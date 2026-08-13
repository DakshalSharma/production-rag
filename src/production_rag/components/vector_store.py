import chromadb
from production_rag.configuration.vector_store_config import VectorStoreConfig
from production_rag.entity.chunk import Chunk
from production_rag.entity.embedding import Embedding



class VectorStore:
    def __init__(self,config:VectorStoreConfig):
        self.config = config
        self.client = chromadb.PersistentClient(
            path = config.persist_directory
        )
        self.collection = self.client.get_or_create_collection(
            name = self.config.collection_name
        )

    def add(self, chunks:list[Chunk],embeddings:list[Embedding])->None:
        if len(chunks)!=len(embeddings):
            raise ValueError
        self.collection.add(
        ids = [chunk.chunk_id for chunk in chunks],
        embeddings = [embedding.vector for embedding in embeddings],
        documents = [chunk.text for chunk in chunks],
        metadatas = [{"source_path":str(chunk.source_path)} for chunk in chunks]
        )

    def search(self, query:list[float],top_k:int=5):
        return self.collection.query(
            query_embeddings=query,
            n_results=top_k
        )





    