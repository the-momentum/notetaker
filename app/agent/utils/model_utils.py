from llama_index.core.llms.llm import LLM
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI

from app.core.config import settings


def get_llm() -> LLM:
    if settings.USE_LOCAL_MODELS:
        return Ollama(
            model=settings.LLM_MODEL,
            request_timeout=360.0,
            base_url=str(settings.OLLAMA_URL),
        )

    return OpenAI(
        model=settings.LLM_MODEL,
        request_timeout=360.0,
        api_key=settings.OPENAI_API_KEY,
    )
