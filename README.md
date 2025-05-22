<a name="readme-top"></a>

<div align="center">
  <img src="https://cdn.prod.website-files.com/66a1237564b8afdc9767dd3d/66df7b326efdddf8c1af9dbb_Momentum%20Logo.svg" height="80">
  <h1>Notetaker AI</h1>
  <p><strong>Intelligent Transcription & Summarization for Professionals</strong></p>

  [![Contact us](https://img.shields.io/badge/Contact%20us-AFF476.svg?style=for-the-badge&logo=mail&logoColor=black)](mailto:hello@themomentum.ai?subject=Notetaker%20AI%20Inquiry)
  [![Visit Momentum](https://img.shields.io/badge/Visit%20Momentum-1f6ff9.svg?style=for-the-badge&logo=safari&logoColor=white)](https://themomentum.ai)
  [![MIT License](https://img.shields.io/badge/License-MIT-636f5a.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
</div>

## 📋 Table of Contents

- [🔍 About](#about-the-project)
- [🚀 Getting Started](#getting-started)
- [📝 Usage](#usage)
- [🖥️ Demo](#demo)
- [🐳 Docker Setup](#docker-setup)
- [🗺️ Roadmap](#roadmap)
- [👥 Contributors](#contributors)
- [📄 License](#license)

## 🔍 About The Project

**Notetaker AI** transforms how professionals handle meetings, interviews, and consultations with advanced audio-to-text capabilities. It combines precise transcription with intelligent summarization to create concise, structured notes that save time and enhance documentation accuracy.

![Notetaker workflow](https://github.com/user-attachments/assets/86774f6d-a39f-42cd-b024-2a2158d36873)

### ✨ Key Features

- **🎙️ Smart Transcription**: Convert audio to text with exceptional accuracy, including optional speaker diarization and time alignment
- **📊 Multiple Summary Formats**: Generate summaries in various formats to fit different professional needs:
  - **📝 Text** – Simple, readable plain-text format  
  - **📋 SOAP** – Structured clinical format (Subjective, Objective, Assessment, Plan)  
  - **🏥 PKI HL7 CDA** – Standards-compliant summary for healthcare interoperability  
  - **🩺 Therapy Assessment** – Custom format for structured evaluation of therapist performance across key professional competencies  
- **⏳ Long-form Audio Support**: Designed to handle recordings of over **1 hour**
- **⚙️ Flexible Deployment**: Can be deployed fully locally, using local AI models for full data control, or using wavaliable external integrations
- **⚙️ Multiple access points**: Run as an API-only service or with an intuitive Gradio UI for interactive use
- **🚄 GPU Acceleration**: Leverage GPU hardware for faster processing of large audio files
- **🔧 Customizable**: Configure to your specific requirements with extensive environment variables

<video src="https://github.com/user-attachments/assets/52b74add-9733-442c-a083-830bfba9d900" controls="controls"></video>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

Follow these steps to set up Notetaker AI in your environment.

### Prerequisites

- **Python**: 3.12 or higher
- **Poetry**: For dependency management ([Installation Guide](https://python-poetry.org/docs/#installation))
- **FFmpeg**: Required for audio processing
- **CUDA Toolkit**: 12.2+ recommended (only if using GPU acceleration)
- **Hugging Face Access**: You'll need access to these gated models:
  - [Speaker Diarization](https://huggingface.co/pyannote/speaker-diarization-3.1)
  - [Segmentation](https://huggingface.co/pyannote/segmentation-3.0)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/the-momentum/notetaker
   cd notetaker
   ```

2. **Install dependencies**:
   ```sh
   # For API only (recommended for production)
   poetry install --without demo --without dev

   # With demo interface (for testing and demonstration)
   poetry install --with demo --without dev
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 Usage

### Configuration

1. **Set up environment variables**:
   ```sh
   cp .env.example .env
   ```
   Edit the `.env` file with your specific configuration.

2. **Start the application**:
   ```sh
   ./run.sh
   ```
   The API will be available at http://localhost:8001 by default.

3. **Access the API documentation**:
   - Swagger UI: http://localhost:8001/docs
   - ReDoc: http://localhost:8001/redoc

### Environment Variables

| Variable | Description | Example Value |
|----------|-------------|---------------|
| PROJECT_NAME | Name used for logging and display | `Notetaker AI` |
| BACKEND_CORS_ORIGINS | Allowed CORS origins | `["http://localhost:8000"]` |
| HOST | Host address for API availability | `0.0.0.0` |
| PORT | Port for the API server | `8001` |
| OLLAMA_URL | Base URL for Ollama server | `http://localhost:11434` |
| LLM_MODEL | LLM model name | `llama3.2` |
| USE_LOCAL_MODELS | Whether to use local models | `True` |
| WHISPER_MODEL | Whisper model type | `turbo` |
| WHISPER_DEVICE | Device for running Whisper | `cpu` or `cuda` |
| WHISPER_COMPUTE_TYPE | Compute type for Whisper | `int8` |
| WHISPER_BATCH_SIZE | Batch size for processing | `16` |
| HF_API_KEY | Hugging Face API key | `hf_...` |
| OPENAI_API_KEY | OpenAI API key | `sk-proj-...` |

⚠️ **Note:** The transcription output length depends on the selected model's token limit. If the transcription is too long, it may be truncated or cause errors. Choose a model appropriate for the expected transcription length to ensure complete results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🖥️ Demo

The interactive Gradio demo provides a user-friendly interface to experience Notetaker AI's capabilities without writing code.

### Running the Demo

1. **Install demo dependencies** (if not already done):
   ```sh
   poetry install --with demo --without dev
   ```

2. **Configure the demo**:
   Update `demo/.env.demo` with your API base URL.

3. **Launch the integrated demo**:
   ```sh
   ./run.sh --demo
   ```
   This starts both the API and Gradio interface.

4. **Or run the demo separately** (if API is already running):
   ```sh
   poetry run python demo/ui.py
   ```

The demo will be available at http://localhost:7860.

### Demo Features

- **📁 Upload or Record**: Submit audio files or record directly in your browser
- **⚙️ Configure Options**: Set parameters for transcription and summarization
- **📊 Format Selection**: Choose between different summary formats
- **⏱️ Real-time Processing**: Watch as your audio is transcribed and summarized
- **💾 Download Results**: Save output as JSON for further use

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🐳 Docker Setup

For consistent deployment across environments, use our Docker setup.

### Quick Commands

```sh
# Build the Docker images
just docker-build

# Rebuild without using cache
just docker-rebuild

# Run the API only
just docker-up

# Run API with Gradio demo
just docker-demo
```

### Access Points

- **API**: http://localhost:8001
- **API Documentation**:
  - Swagger UI: http://localhost:8001/docs
  - ReDoc: http://localhost:8001/redoc
- **Gradio Demo** (if enabled): http://localhost:7860

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🗺️ Roadmap

We're continuously enhancing Notetaker AI with new capabilities. Here's what's on the horizon:

- [ ] **OpenAI API Integration**: Direct connection to Whisper via OpenAI API
- [ ] **Expanded LLM Support**: Integration with additional LLM providers
- [ ] **Enhanced Note Formats**: More specialized formats and improved customization options
- [ ] **Performance Optimizations**: Faster processing for large audio files

Have a suggestion? We'd love to hear from you! Contact us or contribute directly.

## 👥 Contributors

<a href="https://github.com/the-momentum/notetaker/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=the-momentum/notetaker" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <p><em>Built with ❤️ by <a href="https://themomentum.ai">Momentum</a> • Turning conversations into structured knowledge</em></p>
</div>
