"""
AI Assistant Platform V2

Chat Router
"""

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.logger import logger

router = Router(name="chat")


@router.message(CommandStart())
async def start_handler(message: Message):

    logger.info(
        "Start command",
        user_id=message.from_user.id,
    )

    await message.answer(
        """
🤖 <b>AI Assistant Platform V2</b>

Xin chào!

Tôi có thể hỗ trợ:

💬 Chat tự nhiên
📝 Viết content
🎨 Tạo ảnh

Bạn có thể thử:

Tạo ảnh cô gái mặc áo dài

hoặc

Viết caption bán đất

hoặc

Xin chào
"""
    )


@router.message(F.text)
async def message_handler(message: Message):

    logger.info(
        "Receive message",
        user_id=message.from_user.id,
        text=message.text,
    )

    #
    # Sprint 2
    #
    # Intent Service sẽ xử lý tại đây
    #

    await message.answer(
        "🧠 Đã nhận:\n\n"
        f"{message.text}"
    )
