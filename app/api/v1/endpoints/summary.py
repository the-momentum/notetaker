from fastapi import APIRouter, Depends, HTTPException, Query

from app.agent.summarization.service import SummarizationService
from app.schemas.enums import NoteFormat
from app.schemas.summary import SummaryRequest, SummaryResponse

router = APIRouter()


@router.post("/summarize", response_model=SummaryResponse)
async def summarize_transcript(
    summary_request: SummaryRequest,
    format: NoteFormat = Query(default=NoteFormat.TEXT),
    summarization_service: SummarizationService = Depends(),
) -> SummaryResponse:
    """
    Endpoint to summarize a given transcript.

    ### Request Parameters:
    - `summary_request` (SummaryRequest): Contains the transcript to be summarized.
        - The `transcript` field accepts one of the following models:
            - **PlainTextTranscript**:
                ```json
                {
                    "transcript": {
                        "text": "Sample transcript text.",
                        "language": "en"
                    }
                }
                ```
            - **TranscriptionResultModel**:
                ```json
                {
                    "transcript": {
                        "segments": [
                            {
                                "start": 0,
                                "end": 10,
                                "text": "Sample segment text."
                            }
                        ],
                        "language": "en"
                    }
                }
                ```
            - **AlignedTranscriptionResultModel**:
                ```json
                {
                    "transcript": {
                        "segments": [
                            {
                                "start": 0,
                                "end": 10,
                                "text": "Sample segment text."
                            }
                        ],
                        "word_segments": [
                            {
                                "start": 0.1,
                                "end": 0.5,
                                "text": "Sample"
                            }
                        ],
                        "language": "en"
                    }
                }
                ```
    - `format` (NoteFormat): The desired note format

    ### Returns:
    - `SummaryResponse`: Contains the generated summary in the specified format.

    ### Raises:
    - `400 Bad Request`: If the transcript is empty or missing.
    - `500 Internal Server Error`: If the summarization process fails.
    """
    if not summary_request.transcript:
        raise HTTPException(status_code=400, detail="Transcript cannot be empty.")

    try:
        summary = summarization_service.summarize(
            summary_request.transcript,
            format=format,
            language=summary_request.transcript.language,
        )

        if not summary:
            raise HTTPException(status_code=500, detail="Failed to generate a summary.")

        return SummaryResponse(note=summary)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
