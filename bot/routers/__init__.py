"""
Routers
"""

from aiogram import Router

from .chat import router as chat_router


def setup_router() -> Router:

    router = Router()

    router.include_router(chat_router)

    return router
