from dataclasses import dataclass

from production_rag.constants import VECTOR_STORE_PATH, COLLECTION_NAME


@dataclass(frozen=True)
class VectorStoreConfig:
    persist_directory: str = VECTOR_STORE_PATH
    collection_name: str = COLLECTION_NAME