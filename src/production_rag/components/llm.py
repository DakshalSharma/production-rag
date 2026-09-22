from transformers import AutoTokenizer, AutoModelForCausalLM
from production_rag.configuration.llm_config import LLMConfig


class LLM:
    def __init__(self, config: LLMConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(config.model_name)

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.config.max_new_tokens,
            temperature=self.config.temperature,
            do_sample=False
        )
        response = self.tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        return response