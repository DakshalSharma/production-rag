from dataclasses import dataclass
from production_rag.constants import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_OVERLAP,
    SEPARATOR_LIST
)


@dataclass(frozen=True)
class ChunkerConfig:
    chunk_size: int = DEFAULT_CHUNK_SIZE
    chunk_overlap: int = DEFAULT_OVERLAP
    separators: tuple[str,...] = SEPARATOR_LIST
