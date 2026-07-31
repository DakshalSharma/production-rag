from pathlib import Path

from production_rag.configuration.pdf_loader_config import PDFLoaderConfig
from production_rag.pipeline.ingestion_pipeline import IngestionPipeline


config = PDFLoaderConfig()

pipeline = IngestionPipeline(config=config)

pdf_path = "data/sample_pdfs/232796.pdf"


document = pipeline.run(Path(pdf_path))

print(document.text)
print(document.page_count)
print(document.source_path)