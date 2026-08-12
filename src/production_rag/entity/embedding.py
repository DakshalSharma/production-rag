from dataclasses import dataclass


@dataclass(frozen=True)
class Embedding:
    chunk_id:str
    vector:list[float]