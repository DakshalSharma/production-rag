from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.entity.chunk import Chunk
from production_rag.entity.embedding import Embedding
from production_rag.exception.exception import MyException
from production_rag.logging.logger import logger
from sentence_transformers import SentenceTransformer



class EmbeddingGenerator:
    def __init__(self, config: EmbeddingConfig):
        self.config = config
        self.model = SentenceTransformer(config.model)

    def _validate_chunks(self, chunks: list[Chunk]) -> None:
        if not isinstance(chunks, list):
            raise ValueError("Chunks must be a list.")
        if not chunks:
            raise ValueError("Chunk list cannot be empty.")
        for chunk in chunks:
            if not isinstance(chunk, Chunk):
                raise ValueError("All elements must be Chunk objects.")
            if not chunk.text or not chunk.text.strip():
                raise ValueError("Chunk text cannot be empty.")
            if chunk.chunk_id is None:
                raise ValueError("Chunk ID cannot be None.")

    def _generate_embeddings(self, chunks: list[Chunk]) -> list[Embedding]:
        text = [chunk.text for chunk in chunks]
        vectors = self.model.encode(
            text,
            batch_size=self.config.batch_size,
            normalize_embeddings=True
        )
        embeddings = []
        for vector, chunk in zip(vectors,chunks):
            embeddings.append(
                Embedding(
                    chunk_id=chunk.chunk_id,
                    vector=vector.tolist()
                )
            )
        return embeddings
        
        

    # def _generate_embeddings(self, chunks: list[Chunk]) -> list[Embedding]:
    #     embeddings: list[Embedding] = []
    #     for chunk in chunks:
    #         embedding = self._generate_embedding(chunk)
    #         embeddings.append(embedding)
    #     return embeddings

    def embed(self, chunks: list[Chunk]) -> list[Embedding]:
        logger.info("Starting embedding generation.")
        try:
            self._validate_chunks(chunks)
            logger.info("Chunk validation completed.")
            embeddings = self._generate_embeddings(chunks)
            logger.info("Generated %d embeddings.", len(embeddings))
            logger.info("Embedding generation completed successfully.")
            return embeddings
        except Exception as e:
            logger.exception("Embedding generation failed.")
            raise MyException("Embedding generation failed.", e) from e