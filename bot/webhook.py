"""
AI Assistant Platform V2

Telegram Webhook
"""

from fastapi import APIRouter, HTTPException, Request, Response

from aiogram.types import Update

from bot.telegram import telegram_bot
from config import settings
from utils.logger import logger

router = APIRouter()


@router.post("/webhook/{secret}")
async def telegram_webhook(
    secret: str,
    request: Request,
):
    """
    Telegram Webhook Endpoint
    """

    if secret != settings.WEBHOOK_SECRET:
        logger.warning(
            "Invalid webhook secret",
            secret=secret,
        )

        raise HTTPException(
            status_code=403,
            detail="Forbidden",
        )

    try:

        data = await request.json()

        update = Update.model_validate(data)

        await telegram_bot.dp.feed_update(
            telegram_bot.bot,
            update,
        )

        return Response(status_code=200)

    except Exception:

        logger.exception("Webhook processing failed")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        )


@router.get("/health")
async def health():
    """
    Health Check
    """

    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
