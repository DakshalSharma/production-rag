from dataclasses import dataclass
from production_rag.constants import LLM_MODEL


@dataclass(frozen=True)
class LLMConfig:
    model_name: str = LLM_MODEL
    max_new_tokens: int = 256