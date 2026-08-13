from pathlib import Path
from production_rag.components.chunker import Chunker
from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.pdf_loader import PDFLoader
from production_rag.components.vector_store import VectorStore
from production_rag.configuration.chunker_config import ChunkerConfig
from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.configuration.pdf_loader_config import PDFLoaderConfig
from production_rag.configuration.vector_store_config import VectorStoreConfig
from production_rag.pipeline.ingestion_pipeline import IngestionPipeline

pdf_loader = PDFLoader(PDFLoaderConfig())
chunker = Chunker(ChunkerConfig())
embedding = EmbeddingGenerator(EmbeddingConfig())
vector_store = VectorStore(VectorStoreConfig())

pipeline = IngestionPipeline(
    pdf_loader=pdf_loader,
    chunker=chunker,
    embedding=embedding,
    vector_store=vector_store
)

embeddings = pipeline.run(Path("data/sample_pdfs/232796.pdf"))

query_vector = embeddings[7].vector
results = vector_store.search(query_vector, top_k=3)

print(results)
print("Embeddings:", len(embeddings))
print("Stored:", vector_store.collection.count())