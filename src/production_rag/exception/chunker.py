from production_rag.exception.exception import MyException


class ChunkerException(MyException):
    pass


class InvalidChunkConfigurationException(ChunkerException):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidDocumentTypeException(ChunkerException):
    def __init__(self):
        super().__init__("Expected a Document object.")


class EmptyDocumentException(ChunkerException):
    def __init__(self):
        super().__init__("Document contains no text.")


class InvalidDocumentSourceException(ChunkerException):
    def __init__(self):
        super().__init__("Document source path is missing.")


class InvalidPageCountException(ChunkerException):
    def __init__(self):
        super().__init__("Document page count must be greater than zero.")


class ChunkingException(ChunkerException):
    def __init__(self):
        super().__init__("Unexpected error occurred while chunking.")