import logging.config

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.debug import mount_debug_endpoints
from app.middlewares import add_cors_middleware

logging.config.fileConfig(settings.LOGGING_CONF_FILE, disable_existing_loggers=False)

app = FastAPI(title=settings.PROJECT_NAME)

add_cors_middleware(app)

if settings.DEBUG:
    mount_debug_endpoints(app)

app.include_router(api_router, prefix=settings.API_V1_STR)
