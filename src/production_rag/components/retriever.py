from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.vector_store import VectorStore
from production_rag.entity.retrieved_chunk import RetrievedChunk


class Retriever:
    def __init__(self, embedding_generator: EmbeddingGenerator, vector_store: VectorStore):
        self.embedding_generator = embedding_generator
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5):
        query_vector = self.embedding_generator.embed_query(query)
        result = self.vector_store.search(query_vector, top_k)
        retrieved_chunks = []
        for chunk_id,text,metadata,distance in zip(
            result['ids'][0],
            result['documents'][0],
            result['metadatas'][0],
            result['distances'][0]
        ):
            retrieved_chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    text=text,
                    source_path=metadata["source_path"],
                    distance=distance
                )
            )
        return retrieved_chunks