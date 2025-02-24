import whisperx
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.agent.transcription.service import TranscriptionService
from app.schemas.transcription import TranscriptionRequest, TranscriptionResponse

router = APIRouter()


@router.post("/transcribe")
async def transcribe_audio(
    transcription_request: TranscriptionRequest = Depends(),
    audio_file: UploadFile = File(...),
    transcription_service: TranscriptionService = Depends(),
) -> TranscriptionResponse:
    """
    Endpoint to transcribe an audio file.

    **Args:**
    - `align` (bool): Perform word-level alignment. Default is False.
    - `perform_diarization` (bool): Perform speaker diarization. Default is False.
    - `audio_file` (UploadFile): Audio file to be transcribed. \
        Accepted formats are `mp3`, `wav`, and `m4a`.

    **Returns:**
    - `TranscriptionResponse`: Contains the transcript and optionally aligned words \
        or diarized segments.

    **Raises:**
    - `400 Bad Request`: If the uploaded file type is not supported.
    - `500 Internal Server Error`: If transcription or alignment fails.
    """
    if audio_file.content_type not in [
        "audio/mpeg",
        "audio/wav",
        "audio/x-wav",
        "audio/x-m4a",
    ]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Accepted types are mp3, wav, m4a.",
        )

    file_location = f"/tmp/{audio_file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(await audio_file.read())

    transcription_result, audio = transcription_service.transcribe(
        file_path=file_location
    )

    if transcription_request.align:
        transcription_result = transcription_service.align_transcription(
            transcription_result, audio
        )

    if transcription_request.perform_diarization:
        diarized_segments = transcription_service.perform_diarization(audio)
        transcription_result = whisperx.assign_word_speakers(
            diarized_segments, transcription_result
        )

    transcription_service.cleanup_file(file_location)

    return TranscriptionResponse(transcript=transcription_result)
