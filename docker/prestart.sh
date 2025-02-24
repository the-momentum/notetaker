#!/bin/bash

set -e -x

if [ "$USE_LOCAL_MODELS" = "True" ]; then
    python -u scripts/pull_local_model.py
else
    echo "Skipping model pull."
fi

python -u scripts/setup_transcription_models.py
echo "Starting the FastAPI application..."

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8001}

uvicorn app.main:app --host "$HOST" --port "$PORT"
