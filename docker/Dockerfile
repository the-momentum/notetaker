# Stage 1: Build Stage
FROM nvidia/cuda:12.2.2-devel-ubuntu22.04 AS build

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHON_VERSION=3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    ffmpeg \
    python3.12 \
    python3-pip \
    python3.12-venv \
    python-is-python3 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.12 -m ensurepip --upgrade && \
    python3.12 -m pip install --no-cache-dir --upgrade pip setuptools poetry pyopenssl

WORKDIR /app
COPY poetry.lock pyproject.toml ./
COPY .. .
COPY ../.env .env

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi
RUN echo "Looking for site-packages..." && find / -name "site-packages" || echo "No site-packages found."

FROM nvidia/cuda:12.2.2-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHON_VERSION=3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libcudnn8 \
    ffmpeg \
    python3.12 \
    python3-pip \
    python-is-python3 \
    curl && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY --from=build /app /app
COPY --from=build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=build /usr/local/bin /usr/local/bin

COPY docker/prestart.sh /usr/local/bin/prestart.sh
RUN chmod +x /usr/local/bin/prestart.sh

CMD ["/usr/local/bin/prestart.sh"]
