from production_rag.components.retriever import Retriever
from production_rag.components.prompt_builder import PromptBuilder
from production_rag.components.llm import LLM


class RAGPipeline:
    def __init__(self, retriever: Retriever, prompt_builder: PromptBuilder, llm: LLM):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def run(self, query: str, top_k: int = 5) -> str:
       chunks = self.retriever.retrieve(query, top_k)
       prompt = self.prompt_builder.build(chunks=chunks,query=query)
       response = self.llm.generate(prompt)
       return response