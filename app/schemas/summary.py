from pydantic import BaseModel

from app.schemas.types import NoteType, TranscriptInput


class SummaryRequest(BaseModel):
    transcript: TranscriptInput


class SummaryResponse(BaseModel):
    note: NoteType
