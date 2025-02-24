import os

import numpy as np
import whisperx
from numpy.typing import NDArray
from whisperx.types import AlignedTranscriptionResult, TranscriptionResult

from app.core.config import settings


class TranscriptionService:
    def __init__(
        self,
    ):

        self.device = settings.WHISPER_DEVICE
        self.model = whisperx.load_model(
            settings.WHISPER_MODEL,
            device=self.device,
            compute_type=settings.WHISPER_COMPUTE_TYPE,
        )

    def transcribe(
        self, file_path: str
    ) -> tuple[TranscriptionResult, NDArray[np.float32]]:
        """
        Transcribe the audio file.
        """
        try:
            audio = whisperx.load_audio(file_path)
            result = self.model.transcribe(
                audio, batch_size=settings.WHISPER_BATCH_SIZE
            )
            return result, audio
        except Exception as e:
            raise Exception(f"Error during transcription: {str(e)}")

    def align_transcription(
        self,
        transcription_result: TranscriptionResult,
        audio: NDArray[np.float32],
    ) -> AlignedTranscriptionResult:
        """
        Align the transcription result to the audio.
        """
        try:
            model_a, metadata = whisperx.load_align_model(
                language_code=transcription_result["language"],
                device=self.device,
            )
            aligned_result = whisperx.align(
                transcription_result["segments"],
                model_a,
                metadata,
                audio,
                self.device,
                return_char_alignments=False,
            )

            return aligned_result
        except Exception as e:
            raise Exception(f"Error during alignment: {str(e)}")

    def perform_diarization(
        self, audio: NDArray[np.float32]
    ) -> AlignedTranscriptionResult | TranscriptionResult:
        """
        Perform diarization on the audio file.
        """
        try:
            diarize_model = whisperx.DiarizationPipeline(
                use_auth_token=settings.HF_API_KEY,
                device=self.device,
            )
            diarized_segments = diarize_model(audio)
            return diarized_segments
        except Exception as e:
            raise Exception(f"Error during diarization: {str(e)}")

    def cleanup_file(self, file_path: str):
        """
        Delete a file at the specified path.
        """
        if os.path.exists(file_path):
            os.remove(file_path)
