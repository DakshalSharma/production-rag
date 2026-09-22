from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.vector_store import VectorStore
from production_rag.components.retriever import Retriever
from production_rag.components.prompt_builder import PromptBuilder
from production_rag.components.llm import LLM
from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.configuration.vector_store_config import VectorStoreConfig
from production_rag.configuration.llm_config import LLMConfig
from production_rag.pipeline.rag_pipeline import RAGPipeline


embedding = EmbeddingGenerator(EmbeddingConfig())
vector_store = VectorStore(VectorStoreConfig())
retriever = Retriever(embedding, vector_store)
prompt_builder = PromptBuilder()
llm = LLM(LLMConfig())

rag = RAGPipeline(
    retriever=retriever,
    prompt_builder=prompt_builder,
    llm=llm
)

response = rag.run(
    "What methods are used for text detection?",
    top_k=5
)

print(response)