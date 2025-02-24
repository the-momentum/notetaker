#! /bin/bash


set -e

if [ "$USE_LOCAL_MODELS" = "True" ]; then
    poetry run python -u scripts/pull_local_model.py
else
    echo "Skipping model pull."
fi

# Set up transcription models
poetry run python -u scripts/setup_transcription_models.py

# Parse arguments
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8001}
UVICORN_ARGS="--host $HOST --port $PORT"
DEMO=false

for arg in "$@"; do
    case $arg in
        --demo)
            DEMO=true
            ;;
        --host=*)
            HOST="${arg#*=}"
            UVICORN_ARGS="--host $HOST $UVICORN_ARGS"
            ;;
        --port=*)
            PORT="${arg#*=}"
            UVICORN_ARGS="--port $PORT $UVICORN_ARGS"
            ;;
        *)
            UVICORN_ARGS="$UVICORN_ARGS $arg"
            ;;
    esac
done

echo "Starting the FastAPI application..."
if [ "$DEMO" = true ]; then
    poetry run uvicorn app.main:app $UVICORN_ARGS &
    echo "Starting Gradio demo..."
    poetry run python -u demo/ui.py
else
    # Run only the API
    poetry run uvicorn app.main:app $UVICORN_ARGS
fi
