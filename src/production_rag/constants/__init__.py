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

#Chunker

SEPARATOR_LIST = ("\n\n", "\n", " ", "")
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_OVERLAP = 200

#Embedding

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

#Vector Store

VECTOR_STORE_PATH = "artifacts/vector_store"
COLLECTION_NAME = "documents"