from typing import Optional

from pydantic import BaseModel

from app.schemas.whisperx_types_wrappers import (
    AlignedTranscriptionResultModel,
    TranscriptionResultModel,
)


class PlainTextTranscript(BaseModel):
    text: str
    language: Optional[str] = None


class TranscriptionRequest(BaseModel):
    align: bool = False
    perform_diarization: bool = False


class TranscriptionResponse(BaseModel):
    transcript: AlignedTranscriptionResultModel | TranscriptionResultModel
