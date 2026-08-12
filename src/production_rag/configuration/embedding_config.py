from dataclasses import dataclass
from production_rag.constants import EMBEDDING_MODEL


@dataclass(frozen=True)
class EmbeddingConfig:
    model:str = EMBEDDING_MODEL
    batch_size: int = 32