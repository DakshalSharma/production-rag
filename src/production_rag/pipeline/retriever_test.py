from production_rag.components import llm
from production_rag.components.embedding import EmbeddingGenerator
from production_rag.components.prompt_builder import PromptBuilder
from production_rag.components.vector_store import VectorStore
from production_rag.components.retriever import Retriever
from production_rag.configuration.embedding_config import EmbeddingConfig
from production_rag.configuration.llm_config import LLMConfig
from production_rag.configuration.vector_store_config import VectorStoreConfig

embedding_generator = EmbeddingGenerator(EmbeddingConfig())
vector_store = VectorStore(VectorStoreConfig())
prompt_builder = PromptBuilder()
llm = llm.LLM(LLMConfig())
retriever = Retriever(
    embedding_generator=embedding_generator,
    vector_store=vector_store
)
query="What are the methods used for text detection and extraction from images and PDFs?"
results = retriever.retrieve(
    query,
    top_k=5
)
prompt = prompt_builder.build(results,query)
answer = llm.generate(prompt)
print(answer)

