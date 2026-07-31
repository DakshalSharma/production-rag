from pathlib import Path

from production_rag.utils import bytes_to_mb


class PDFLoaderException(Exception):
    """Base exception for all PDF loader related exceptions."""
    pass


class PDFFileNotFoundException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"The PDF '{pdf_path}' does not exist."
        )

        super().__init__(message)


class PDFNotAFileException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"The path '{pdf_path}' is not a file."
        )

        super().__init__(message)


class InvalidPDFExtensionException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"The file '{pdf_path}' is not a valid PDF."
        )

        super().__init__(message)


class PDFFileTooLargeException(PDFLoaderException):
    def __init__(
        self,
        pdf_path: Path,
        pdf_size: int,
        max_size: int,
    ):
        self.pdf_path = pdf_path
        self.pdf_size = pdf_size
        self.max_size = max_size

        pdf_size_mb = bytes_to_mb(pdf_size)
        max_size_mb = bytes_to_mb(max_size)

        message = (
            f"The PDF '{pdf_path}' exceeds the maximum allowed size.\n"
            f"Uploaded Size : {pdf_size_mb:.2f} MB\n"
            f"Maximum Size  : {max_size_mb:.2f} MB"
        )

        super().__init__(message)


class PDFCorruptedException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"The PDF '{pdf_path}' is corrupted or has an invalid structure."
        )

        super().__init__(message)


class PDFPasswordProtectedException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"The PDF '{pdf_path}' is password protected and cannot be processed."
        )

        super().__init__(message)


class PDFExtractionException(PDFLoaderException):
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

        message = (
            f"Failed to extract text from '{pdf_path}' due to an unexpected error."
        )

        super().__init__(message)