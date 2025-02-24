from ollama import Client

from app.core.config import settings

if __name__ == "__main__":
    ollama_url = settings.OLLAMA_URL
    model_name = settings.LLM_MODEL

    try:
        client = Client(host=ollama_url)
        print(f"Pulling model '{model_name}' from Ollama at '{ollama_url}'...")
        client.pull(model_name)
        print(f"Successfully pulled model '{model_name}'.")
    except Exception as e:
        print(f"Failed to pull model '{model_name}': {e}")
