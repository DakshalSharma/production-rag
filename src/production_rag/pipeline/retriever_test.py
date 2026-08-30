from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.vector_store import VectorStore
from production_rag.components.retriever import Retriever
from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.configuration.vector_store_config import VectorStoreConfig

embedding_generator = EmbeddingGenerator(EmbeddingConfig())
vector_store = VectorStore(VectorStoreConfig())

retriever = Retriever(
    embedding_generator=embedding_generator,
    vector_store=vector_store
)

results = retriever.retrieve(
    query="What are the methods used for text detection and extraction from images and PDFs?",
    top_k=5
)

print(results)