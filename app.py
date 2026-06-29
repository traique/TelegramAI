"""
AI Assistant Platform V2

Application Entry Point
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from bot.telegram import telegram_bot
from bot.webhook import router as webhook_router
from config import settings
from utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup / Shutdown
    """

    logger.info("===================================")
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Version : {settings.APP_VERSION}")
    logger.info("===================================")

    await telegram_bot.start()

    yield

    logger.info("Stopping application...")

    await telegram_bot.stop()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Register Routers
app.include_router(webhook_router)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "debug": settings.DEBUG,
    }
