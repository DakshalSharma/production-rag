from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    text:str
    page_count:int
    source_path:str
