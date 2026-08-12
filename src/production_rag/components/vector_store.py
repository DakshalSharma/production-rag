import chromadb
from production_rag.configuration.vector_store_config import VectorStoreConfig


class VectorStore:
    def __init__(self,config:VectorStoreConfig):
        self.config = config
        self.client = chromadb.PersistentClient(
            path = config.persist_directory
        )
        self.collection = self.client.get_or_create_collection(
            name = self.config.collection_name
        )

    