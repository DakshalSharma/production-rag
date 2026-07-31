from pathlib import Path

#Logger

LOG_DIR = Path("logs")
ERROR_LOG_FILE = LOG_DIR/"error.log"

#PDF Loader

DEFAULT_MAX_PDF_SIZE = 50.0
ALLOWED_EXTENSIONS = (
    ".pdf",
)
PDF_LOADER_ARTIFACT_DIR = "artifact/pdf_loader"