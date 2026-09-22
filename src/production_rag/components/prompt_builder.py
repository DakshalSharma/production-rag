from production_rag.entity.retrieved_chunk import RetrievedChunk


class PromptBuilder:
    def build_prompt(self,chunks:list[RetrievedChunk])->str:
        return"\n\n".join(chunk.text for chunk in chunks)

    def build(self,chunks:list[RetrievedChunk],query:str):
        context = self.build_prompt(chunks)
        prompt = f"""
Answer the given question based on the provided context only. If the answer cannot be found in the context, say that you don't know.Don't repeat context in your answer.Answer in Maximum 100 Words
context={context}
question={query}
"""
        return prompt
