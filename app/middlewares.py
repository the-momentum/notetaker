from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def add_cors_middleware(app: FastAPI):
    cors_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]
    if settings.BACKEND_CORS_ALLOW_ALL:
        cors_origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_middlewares(app: FastAPI):
    add_cors_middleware(app)
