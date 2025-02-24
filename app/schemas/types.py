from app.schemas.note import PKIHL7CDANote, SOAPNote
from app.schemas.transcription import PlainTextTranscript
from app.schemas.whisperx_types_wrappers import (
    AlignedTranscriptionResultModel,
    TranscriptionResultModel,
)

NoteType = str | SOAPNote | PKIHL7CDANote
TranscriptInput = (
    PlainTextTranscript | TranscriptionResultModel | AlignedTranscriptionResultModel
)
