import whisperx

from app.core.config import settings

if __name__ == "__main__":
    print("Initializing transcription models...")
    _ = whisperx.load_model(
        settings.WHISPER_MODEL,
        device=settings.WHISPER_DEVICE,
        compute_type=settings.WHISPER_COMPUTE_TYPE,
    )
    _, _ = whisperx.load_align_model(
        language_code="en",
        device=settings.WHISPER_DEVICE,
    )
    _ = whisperx.DiarizationPipeline(
        use_auth_token=settings.HF_API_KEY, device=settings.WHISPER_DEVICE
    )
    print("Successfully initialized transcription models.")
