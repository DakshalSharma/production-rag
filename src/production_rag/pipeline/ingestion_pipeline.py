from pathlib import Path
from production_rag.components.chunker import Chunker
from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.pdf_loader import PDFLoader
from production_rag.entity.embedding import Embedding
from production_rag.entity.chunk import Chunk
from production_rag.entity.document import Document


class IngestionPipeline():
    def __init__(
            self,
            pdf_loader:PDFLoader,
            chunker:Chunker,
            embedding:EmbeddingGenerator
    ):
        self.pdf_loader = pdf_loader
        self.chunker = chunker
        self.embedding = embedding

    def run(self, pdf_path:Path):
        document:Document = self.pdf_loader.load(pdf_path)
        chunks:Chunk = self.chunker.chunk(document)
        embedding:Embedding = self.embedding.embed(chunks)
        return embedding

