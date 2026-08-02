from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    text: str
    source_path: str
    chunk_id: str