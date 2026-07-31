from dataclasses import dataclass
from pathlib import Path
import fitz
from production_rag.configuration import PDFLoaderConfig
from production_rag.entity import Document
from production_rag.exception import (
    PDFCorruptedException,
    PDFExtractionException,
    PDFFileNotFoundException,
    PDFFileTooLargeException,
    InvalidPDFExtensionException,
    PDFNotAFileException,
    PDFPasswordProtectedException,
)
from production_rag.logging import logger


@dataclass(frozen=True)
class ExtractedPDF:
    text: str
    page_count: int


class PDFLoader:
    def __init__(self, config: PDFLoaderConfig):
        self.config = config

    def _validate_path_exists(self, pdf_path: Path) -> None:
        if not pdf_path.exists():
            raise PDFFileNotFoundException(pdf_path)

    def _validate_is_file(self, pdf_path: Path) -> None:
        if not pdf_path.is_file():
            raise PDFNotAFileException(pdf_path)

    def _validate_extension(self, pdf_path: Path) -> None:
        if pdf_path.suffix.lower() not in self.config.allowed_extensions:
            raise InvalidPDFExtensionException(pdf_path)

    def _validate_file_size(self, pdf_path: Path) -> None:
        pdf_size = pdf_path.stat().st_size

        if pdf_size > self.config.max_pdf_size_bytes:
            raise PDFFileTooLargeException(
                pdf_path,
                pdf_size=pdf_size,
                expected_size=self.config.max_pdf_size_bytes,
            )

    def _extract_text(self, pdf_path: Path) -> ExtractedPDF:
        logger.info("Starting text extraction from PDF: %s", pdf_path)

        try:
            with fitz.open(pdf_path) as document:

                if document.needs_pass:
                    raise PDFPasswordProtectedException(pdf_path)

                page_texts: list[str] = []

                for page in document:
                    page_texts.append(page.get_text("text"))

                logger.info(
                    "Successfully extracted %d pages from PDF: %s",
                    document.page_count,
                    pdf_path,
                )

                return ExtractedPDF(
                    text="\n".join(page_texts),
                    page_count=document.page_count,
                )

        except fitz.FileDataError as e:
            raise PDFCorruptedException(pdf_path) from e

        except RuntimeError as e:
            raise PDFExtractionException(pdf_path) from e

    def _build_document(
        self,
        pdf_path: Path,
        extracted_pdf: ExtractedPDF,
    ) -> Document:

        logger.info("Building Document entity for PDF: %s", pdf_path)

        return Document(
            text=extracted_pdf.text,
            page_count=extracted_pdf.page_count,
            source_path=str(pdf_path),
        )

    def _validate_file(self, pdf_path: Path) -> None:
        self._validate_path_exists(pdf_path)
        self._validate_is_file(pdf_path)
        self._validate_extension(pdf_path)
        self._validate_file_size(pdf_path)

    def load(self, pdf_path: Path) -> Document:
        logger.info("Loading PDF: %s", pdf_path)

        self._validate_file(pdf_path)

        extracted_pdf = self._extract_text(pdf_path)

        document = self._build_document(
            pdf_path=pdf_path,
            extracted_pdf=extracted_pdf,
        )

        logger.info("Successfully loaded PDF: %s", pdf_path)

        return document