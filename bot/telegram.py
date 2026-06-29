"""
AI Assistant Platform V2

Telegram Manager

Quản lý Bot + Dispatcher.
"""

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.routers import setup_router
from config import settings
from utils.logger import logger


class TelegramBot:

    def __init__(self):

        self.bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
        )

        self.dp = Dispatcher()

        self.dp.include_router(
            setup_router()
       )
    async def start(self):

        logger.info("Initializing Telegram Dispatcher...")

        bot_info = await self.bot.get_me()

        logger.info(
            "Telegram connected",
            username=bot_info.username,
            id=bot_info.id,
        )

    async def stop(self):

        logger.info("Closing Telegram Bot...")

        await self.bot.session.close()


telegram_bot = TelegramBot()
