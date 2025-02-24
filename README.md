<a name="readme-top"></a>

<div align=center>
  <img src="https://cdn.prod.website-files.com/66a1237564b8afdc9767dd3d/66df7b326efdddf8c1af9dbb_Momentum%20Logo.svg" height="64">
</div>
<h1 align=center>Notetaker AI</h1>
<div align=center>
  <a href=mailto:hello@themomentum.ai?subject=Notetaker%20AI%20Inquiry>
    <img src=https://img.shields.io/badge/Contact%20us-AFF476.svg alt="Contact us">
  </a>
    <a href="https://themomentum.ai">
    <img src=https://img.shields.io/badge/Check%20Momentum-1f6ff9.svg alt="Check">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-636f5a.svg?longCache=true" alt="MIT License">
  </a>
</div>
<br>

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#docker-setup">Docker Setup</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---

## About The Project

**Notetaker AI** is an AI-powered transcription and summarization tool designed for professionals. It supports advanced audio-to-text transcription with speaker diarization and alignment, along with flexible summarization in various formats.

### Features

- Accurate audio transcription with optional speaker diarization and alignment.
- Summarization in multiple formats (Text, SOAP, PKI HL7 CDA).
- Flexible configuration to run API-only or API with Gradio UI demo.
- GPU support for faster model inference.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.12+
- Poetry ([Installation Guide](https://python-poetry.org/docs/#installation))
- FFmpeg
- CUDA Toolkit (12.2+ recommended) *(required only if using GPU for model inference)*
- Access to gated pyannote models on Hugging Face:
  - [Speaker Diarization](https://huggingface.co/pyannote/speaker-diarization-3.1)
  - [Segmentation](https://huggingface.co/pyannote/segmentation-3.0)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/the-momentum/notetaker
   cd notetaker
   ```

2. Install core dependencies: To install only the dependencies required for the core API (excluding demo and development dependencies), use:
    ```sh
    poetry install --without demo --without dev
    ```

## Usage

1. Set up environment variables:
    Copy the provided `.env.example` file to `.env`:
    ```sh
    cp .env.example .env
    ```

    Update the .env file with your configuration values.

2. Run the application:
    Use the provided run.sh script to start the API:
    ```sh
    ./run.sh
    ```
    By default, the application will run on http://localhost:8001.

3. Access API documentation:

    Swagger UI: Available at http://localhost:8001/docs

    ReDoc: Available at http://localhost:8001/redoc

These interfaces provide detailed documentation of all available endpoints, request formats, and responses.

### Environment variables
| Variable                 | Example Value                                                        | Description                                                                                     |
|--------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| PROJECT_NAME             | Notetaker AI                                                     | The name of the project, used for logging and display purposes.                                |
| BACKEND_CORS_ORIGINS     | [`http://localhost:8000`, `https://localhost:8000`, `http://localhost`, `https://localhost`] | A list of allowed origins for CORS (Cross-Origin Resource Sharing). Adjust for your front-end. |
| HOST                     | 0.0.0.0                                                         | The host address where the API will be available. Use "0.0.0.0" to listen on all network interfaces. |
| PORT                     | 8001                                                               | The port on which the API will run.                                                            |
| OLLAMA_URL               | `http://localhost:11434`                                           | The base URL for the Ollama server. Used for LLM (Language Model) requests when `USE_LOCAL_MODELS` is set to `True`. Change to `http://ollama:11434` if using Docker setup.                 |
| LLM_MODEL                | llama3.2                                                        | The name of the LLM model to be used.                                                          |
| USE_LOCAL_MODELS         | True                                                               | Whether to use local models for transcription and summarization.                               |
| WHISPER_MODEL            | turbo                                                           | The model type for Whisper (e.g., "base", "large", "turbo").  Refer to [available models](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages).                                 |
| WHISPER_DEVICE           | cpu                                                             | The device for running Whisper (e.g., "cpu", "cuda").                                           |
| WHISPER_COMPUTE_TYPE     | int8                                                            | The compute type for Whisper, affecting performance and precision (e.g., "int8", "float32"). Use "int8" if low GPU memory.  |
| WHISPER_BATCH_SIZE       | 16                                                           |  The batch size for Whisper processing. Reduce the number if low on GPU memory.  |
| HF_API_KEY               | `hf_...`                                                     | The API key for accessing Hugging Face models and resources.                                   |
| OPENAI_API_KEY           | `sk-proj-...`                                                 | The API key for OpenAI's services, used for LLM when `USE_LOCAL_MODELS` is set to `False`.                             |

Refer to the Demo section for instructions on running the application with the Gradio demo interface.

## Demo

The Gradio demo provides an interactive interface to test Notetaker AI's capabilities, including transcription and summarization, directly in your browser.

### Prerequisites

To run the demo, ensure the following dependencies are installed in addition to the core requirements:

```sh
poetry install --with demo --without dev
```

### Running the Demo

Update `demo/.env.demo` with the appropriate API_BASE_URL (e.g., http://localhost:8001).

#### Start the Demo

To run both the API and Gradio demo together:
```sh
./run.sh --demo
```

By default, the demo will run on http://localhost:7860.

#### Standalone Demo
If the API is already running, you can start the Gradio demo separately:
```sh
poetry run python demo/ui.py
```


### Features of the Demo

- Upload or record audio directly in the interface.
- Configure options for speaker diarization and alignment.
- Select desired summary format (Text, SOAP, PKI HL7 CDA).
- View real-time transcription and summary outputs.
- Download the generated summary as a JSON file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Docker Setup

The project supports a Dockerized setup for ease of deployment. Using the provided docker-compose configuration, you can quickly run the API and the Gradio demo.

### Running the Services

You can use the provided Makefile for convenience:
- Build the Docker Images:
```sh
make docker-build
```
- Rebuild without cache:
```sh
make docker-rebuild
```
Run the API:
```sh
make docker-up
```
Run the API with the Gradio Demo:
```sh
make docker-demo
```

### Notes

  By default, the API will be available at http://localhost:8001, and its documentation can be accessed at:
      Swagger UI: http://localhost:8001/docs
      ReDoc: http://localhost:8001/redoc
  The Gradio demo (if enabled) will run on http://localhost:7860.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

We are actively working to enhance Notetaker AI with new features and capabilities. Here's what's planned for the future:

- [] Integration with Whisper via OpenAI API
- [] Support for More LLM Providers
- [] Introduce more note formats and refine the current options for better customization and usability

If you have suggestions or feature requests, feel free to contribute or contact us.

## Contributors

<a href="https://github.com/the-momentum/notetaker/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=the-momentum/notetaker" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

*Built with ❤️ by [Momentum](https://themomentum.ai)*
