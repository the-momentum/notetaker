from typing import Any, Optional, Type

from pydantic import BaseModel

from app.agent.prompts import prompt_manager
from app.agent.utils.model_utils import get_llm
from app.schemas.enums import NoteFormat
from app.schemas.note import PKIHL7CDANote, SOAPNote
from app.schemas.transcription import PlainTextTranscript
from app.schemas.types import TranscriptInput
from app.schemas.whisperx_types_wrappers import (
    AlignedTranscriptionResultModel,
    TranscriptionResultModel,
)


class SummarizationService:
    """
    Service to summarize a transcript using a language model.
    """

    def __init__(self):
        self.llm = get_llm()
        self.summarize_prompt = prompt_manager.get_prompt("summarize")

    def _prepare_transcript(self, transcript: TranscriptInput) -> str:
        """
        Convert structured transcript data to plain text if needed.
        """
        if isinstance(transcript, PlainTextTranscript):
            return transcript.text
        elif isinstance(transcript, TranscriptionResultModel) or isinstance(
            transcript, AlignedTranscriptionResultModel
        ):
            return " ".join(segment.text for segment in transcript.segments)
        else:
            raise ValueError("Unsupported transcript format.")

    def _replace_empty_strings_with_none(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Recursively replace empty string values with None in a nested dictionary.
        """
        for key, value in data.items():
            if isinstance(value, str) and value == "":
                data[key] = None
            elif isinstance(value, dict):
                data[key] = self._replace_empty_strings_with_none(value)
        return data

    def summarize(
        self,
        transcript: TranscriptInput,
        format: NoteFormat,
        language: Optional[str] = None,
    ) -> Optional[str | BaseModel]:
        """
        Generate a summary from a given transcript.
        """
        if not transcript:
            return None

        if not self.summarize_prompt:
            raise ValueError("Summarization prompt not found.")

        transcript_text = self._prepare_transcript(transcript)
        prompt = self.summarize_prompt.format(
            transcript=transcript_text, target_language=language
        )

        structured_models: dict[NoteFormat, Type[BaseModel]] = {
            NoteFormat.SOAP: SOAPNote,
            NoteFormat.PKI_HL7_CDA: PKIHL7CDANote,
        }

        if format in structured_models:
            sllm = self.llm.as_structured_llm(structured_models[format])
            response = sllm.complete(prompt)

            if response and response.raw:
                structured_data = structured_models[format].model_dump(response.raw)
                parsed_data = self._replace_empty_strings_with_none(structured_data)
                return structured_models[format](**parsed_data)
            else:
                return None

        response = self.llm.complete(prompt)
        return response.text if response else None
