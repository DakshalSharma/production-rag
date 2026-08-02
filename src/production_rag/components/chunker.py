from production_rag.logging.logger import logger
from production_rag.configuration.chunker_config import ChunkerConfig
from production_rag.entity.chunk import Chunk
from production_rag.entity.document import Document
from production_rag.exception.chunker import (
    InvalidChunkConfigurationException,
    ChunkingException,
)


class Chunker:
    def __init__(self, config: ChunkerConfig):
        self.config = config
        self._validate_config()

    def _validate_config(self) -> None:
        if self.config.chunk_size <= 0:
            raise InvalidChunkConfigurationException("Chunk size must be greater than zero.")
        if self.config.chunk_overlap < 0:
            raise InvalidChunkConfigurationException("Chunk overlap cannot be negative.")
        if self.config.chunk_overlap >= self.config.chunk_size:
            raise InvalidChunkConfigurationException("Chunk overlap must be smaller than chunk size.")

    def _validate_document(self, document: Document) -> None:
        if not isinstance(document, Document):
            raise ChunkingException()
        if not document.text or not document.text.strip():
            raise ChunkingException()
        if not document.source_path:
            raise ChunkingException()
        if document.page_count <= 0:
            raise ChunkingException()

    def _character_splitter(self, text: str) -> list[str]:
        chunks: list[str] = []
        chunk_size = self.config.chunk_size
        step = chunk_size - self.config.chunk_overlap
        start = 0
        while start < len(text):
            chunks.append(text[start:start + chunk_size])
            start += step
        return chunks

    def _recursive_splitter(self, text: str, separator_index: int) -> list[str]:
        if len(text) <= self.config.chunk_size:
            return [text]
        if separator_index >= len(self.config.separators):
            return self._character_splitter(text)
        separator = self.config.separators[separator_index]
        parts = text.split(separator)
        result: list[str] = []
        for part in parts:
            if not part.strip():
                continue
            if len(part) <= self.config.chunk_size:
                result.append(part)
            else:
                result.extend(self._recursive_splitter(part, separator_index + 1))
        return result

    def _merge(self, chunks: list[str]) -> list[str]:
       merged_chunks: list[str] = []
       current_chunk = ""
       overlap = self.config.chunk_overlap
       for chunk in chunks:
           if not current_chunk:
               current_chunk = chunk
           elif len(current_chunk) + len(chunk) <= self.config.chunk_size:
               current_chunk += chunk
           else:
               merged_chunks.append(current_chunk)
               current_chunk = current_chunk[-overlap:] + chunk
       if current_chunk:
           merged_chunks.append(current_chunk)
       return merged_chunks
                
       

    def _create_chunks(self, chunks: list[str], document: Document) -> list[Chunk]:
        chunk_list: list[Chunk] = []
        for index, text in enumerate(chunks):
            chunk_list.append(
                Chunk(
                    chunk_id=str(index),
                    source_path=document.source_path,
                    text=text
                )
            )
        return chunk_list

    def chunk(self, document: Document) -> list[Chunk]:
        logger.info("Starting document chunking.")
        try:
            self._validate_document(document)
            logger.info("Document validation completed.")
            split_chunks = self._recursive_splitter(document.text, 0)
            logger.info("Recursive splitter generated %d text chunks.", len(split_chunks))
            merged_chunks = self._merge(split_chunks)
            logger.info("Merged into %d chunks.", len(merged_chunks))
            chunk_objects = self._create_chunks(merged_chunks, document)
            logger.info("Created %d Chunk objects.", len(chunk_objects))
            logger.info("Document chunking completed successfully.")
            return chunk_objects
        except Exception as e:
            logger.exception("Unexpected error occurred during chunking.")
            raise ChunkingException() from e