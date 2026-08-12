from pathlib import Path

from production_rag.components.chunker import Chunker
from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.pdf_loader import PDFLoader
from production_rag.configuration.chunker_config import ChunkerConfig
from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.configuration.pdf_loader_config import PDFLoaderConfig
from production_rag.pipeline.ingestion_pipeline import IngestionPipeline

pdf_loader = PDFLoader(PDFLoaderConfig())
chunker = Chunker(ChunkerConfig())
embedding = EmbeddingGenerator(EmbeddingConfig)



pipeline = IngestionPipeline(pdf_loader=pdf_loader,chunker=chunker,embedding=embedding)

pdf_path = "data/sample_pdfs/232796.pdf"


embeddings = pipeline.run(Path(pdf_path))

for embedding in embeddings:
    print(embedding.vector[0])