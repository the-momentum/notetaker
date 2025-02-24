import os
from typing import Any, Callable, Generator, List, Optional, Union

from pydantic.v1 import AnyHttpUrl, BaseSettings, validator

CallableGenerator = Generator[Callable[..., Any], None, None]


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    VERSION: str = "0.0.1"

    DEBUG: bool = False

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    BACKEND_CORS_ALLOW_ALL: bool = False

    # AGENT

    # Integrations
    OPENAI_API_KEY: str
    OLLAMA_URL: Optional[AnyHttpUrl] = None
    HF_API_KEY: str

    # Models
    WHISPER_MODEL: str
    WHISPER_DEVICE: str
    WHISPER_COMPUTE_TYPE: str
    WHISPER_BATCH_SIZE: int

    LLM_MODEL: str
    USE_LOCAL_MODELS: bool

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    LOGGING_CONF_FILE: str = "logging.conf"

    class Config:
        case_sensitive = True
        env_file = os.environ.get("ENV", ".env")


settings = Settings()  # type: ignore
