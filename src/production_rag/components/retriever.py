from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.vector_store import VectorStore


class Retriever:
    def __init__(self, embedding_generator: EmbeddingGenerator, vector_store: VectorStore):
        self.embedding_generator = embedding_generator
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5):
        query_vector = self.embedding_generator.embed_query(query)
        return self.vector_store.search(query_vector, top_k)