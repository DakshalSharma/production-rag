from dataclasses import dataclass,field
from production_rag.constants import (
    DEFAULT_MAX_PDF_SIZE,
    ALLOWED_EXTENSIONS,
    PDF_LOADER_ARTIFACT_DIR
)
from production_rag.utils import mb_to_bytes


@dataclass(frozen=True)
class PDFLoaderConfig:
    allowed_extensions:tuple[str,...] = ALLOWED_EXTENSIONS
    max_pdf_size_mb:int = DEFAULT_MAX_PDF_SIZE
    artifact_dir:str = PDF_LOADER_ARTIFACT_DIR
    max_pdf_size_bytes:int = field(init=False)

    def __post_init__(self):
        normalized_extensions = tuple(
            extension.lower()
            for extension in self.allowed_extensions
        )
        pdf_size_bytes = mb_to_bytes(self.max_pdf_size_mb)
        object.__setattr__(
            self,
            "max_pdf_size_bytes",
            pdf_size_bytes
        )
        object.__setattr__(
            self,
            "allowed_extensions",
            normalized_extensions
        )