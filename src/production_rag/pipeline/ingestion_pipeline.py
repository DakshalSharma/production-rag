from pathlib import Path
from production_rag.components.pdf_loader import PDFLoader
from production_rag.configuration import PDFLoaderConfig


class IngestionPipeline():
    def __init__(self, config:PDFLoaderConfig):
        self.pdf_loader = PDFLoader(config)

    def run(self, pdf_path:Path):
        return self.pdf_loader.load(pdf_path)

