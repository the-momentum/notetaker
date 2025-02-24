from fastapi import APIRouter

from app.api.v1.endpoints import summary, transcript

api_router = APIRouter()
api_router.include_router(transcript.router, prefix="/note", tags=["note"])
api_router.include_router(summary.router, prefix="/note", tags=["note"])


@api_router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
