import json
import os
from typing import Any

import gradio as gr
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api/v1")


def format_time(seconds: float) -> str:
    """
    Convert seconds into MM:SS format.
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02}:{secs:02}"


def format_transcription(transcript_json: dict[str, Any]) -> str:
    """
    Format transcription output for display.
    """
    formatted_transcription = []

    for segment in transcript_json.get("segments", []):
        speaker = segment.get("speaker", None)
        start_time = format_time(segment["start"])
        end_time = format_time(segment["end"])
        text = segment["text"]

        if speaker:
            formatted_line = f"{speaker.upper()} [{start_time}-{end_time}]: {text}"
        else:
            formatted_line = f"[{start_time}-{end_time}]: {text}"

        formatted_transcription.append(formatted_line)

    return "\n".join(formatted_transcription)


def format_summary(summary: str | dict[str, Any], indent: int = 0) -> str:
    """
    Recursively format a nested dictionary into a human-readable string.
    """
    if not isinstance(summary, dict):
        return str(summary)

    formatted_summary = []
    indent_space = " " * (indent * 4)

    for key, value in summary.items():
        formatted_key = f"{indent_space}{key.replace('_', ' ').capitalize()}:"

        if isinstance(value, dict):
            formatted_value = format_summary(value, indent + 1)
            formatted_summary.append(f"{formatted_key}\n{formatted_value}\n")
        elif isinstance(value, list):
            formatted_value = "\n".join(f"{indent_space}    - {item}" for item in value)
            formatted_summary.append(f"{formatted_key}\n{formatted_value}")
        else:
            formatted_value = str(value) if value is not None else "Not provided"
            formatted_summary.append(f"{formatted_key} {formatted_value}")

    return "\n".join(formatted_summary)


def process_audio(
    audio_file: str, align: bool, diarization: bool, summary_format: str
) -> tuple[str, str, str]:
    """
    Process uploaded audio file: transcribe and summarize via API calls.
    """
    if not audio_file:
        raise gr.Error(
            "No audio file provided. Please upload a file or record audio.",
            duration=10,
        )

    transcribe_url = f"{API_BASE_URL}/note/transcribe"
    summarize_url = f"{API_BASE_URL}/note/summarize"

    try:
        with open(audio_file, "rb") as file:
            actual_filename = os.path.basename(audio_file)
            files = [("audio_file", (actual_filename, file, "audio/wav"))]
            transcribe_response = requests.post(
                transcribe_url,
                files=files,
                params={"align": align, "perform_diarization": diarization},
            )
            transcribe_response.raise_for_status()
            transcript = transcribe_response.json().get("transcript", "")
            formatted_transcription = format_transcription(transcript)
    except Exception as e:
        raise gr.Error(f"Error during transcription: {str(e)}", duration=10)

    try:
        summarize_response = requests.post(
            summarize_url,
            json={"transcript": transcript},
            params={"format": summary_format},
        )
        summarize_response.raise_for_status()
        response = summarize_response.json()
        summary = response.get("note", "")

        file_path = "note.json"
        with open(file_path, "w") as f:
            json.dump(response, f, indent=4)

        formatted_summary = format_summary(summary)
    except Exception as e:
        raise gr.Error(f"Error during summarization: {str(e)}", duration=10)

    return formatted_transcription, formatted_summary, file_path


with gr.Blocks() as interface:
    gr.Markdown("## Notetaker AI Demo")

    with gr.Row():
        with gr.Column():
            gr.Markdown("## Audio")
            audio_input = gr.Audio(
                type="filepath",
                sources=["microphone", "upload"],
                label="Upload or record audio",
            )
            align_checkbox = gr.Checkbox(label="Enable Alignment", value=False)
            diarization_checkbox = gr.Checkbox(label="Enable Diarization", value=False)
            summary_format_dropdown = gr.Dropdown(
                choices=["Text", "SOAP", "PKI HL7 CDA"],
                label="Select Note Format",
            )
            submit_button = gr.Button("Submit")

        with gr.Column():
            gr.Markdown("## Transcript")
            transcription_output = gr.Textbox(lines=10, interactive=False, label="")

            gr.Markdown("## Note")
            summary_output = gr.TextArea(value="", label="")
            download_button = gr.DownloadButton(label="Download Note")

    submit_button.click(
        fn=process_audio,
        inputs=[
            audio_input,
            align_checkbox,
            diarization_checkbox,
            summary_format_dropdown,
        ],
        outputs=[transcription_output, summary_output, download_button],
    )

if __name__ == "__main__":
    interface.launch()
