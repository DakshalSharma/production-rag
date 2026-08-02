from pathlib import Path

from production_rag.components.chunker import Chunker
from production_rag.components.pdf_loader import PDFLoader
from production_rag.configuration.chunker_config import ChunkerConfig
from production_rag.configuration.pdf_loader_config import PDFLoaderConfig
from production_rag.pipeline.ingestion_pipeline import IngestionPipeline

pdf_loader = PDFLoader(PDFLoaderConfig())
chunker = Chunker(ChunkerConfig())


pipeline = IngestionPipeline(pdf_loader=pdf_loader,chunker=chunker)

pdf_path = "data/sample_pdfs/232796.pdf"


document = pipeline.run(Path(pdf_path))

for chunk in document:
    print("-" * 80)
    print(f"Chunk ID   : {chunk.chunk_id}")
    print(f"Source     : {chunk.source_path}")
    print(f"Length     : {len(chunk.text)}")
    print(chunk.text[:200])