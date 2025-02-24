from typing import List, Optional

from pydantic import BaseModel


class SingleWordSegmentModel(BaseModel):
    """
    A single word of a speech.
    """

    word: str
    start: Optional[float] = None
    end: Optional[float] = None
    score: Optional[float] = None
    speaker: Optional[str] = None


class SingleCharSegmentModel(BaseModel):
    """
    A single char of a speech.
    """

    char: str
    start: float
    end: float
    score: float


class SingleSegmentModel(BaseModel):
    """
    A single segment (up to multiple sentences) of a speech.
    """

    start: float
    end: float
    text: str
    speaker: Optional[str] = None


class SingleAlignedSegmentModel(BaseModel):
    """
    A single segment (up to multiple sentences) of a speech with word alignment.
    """

    start: float
    end: float
    text: str
    words: List[SingleWordSegmentModel]
    chars: Optional[List[SingleCharSegmentModel]] = None
    speaker: Optional[str] = None


class TranscriptionResultModel(BaseModel):
    """
    A list of segments and word segments of a speech.
    """

    segments: List[SingleSegmentModel]
    language: str


class AlignedTranscriptionResultModel(BaseModel):
    """
    A list of segments and word segments of a speech.
    """

    segments: List[SingleAlignedSegmentModel]
    word_segments: List[SingleWordSegmentModel]
    language: Optional[str] = None
