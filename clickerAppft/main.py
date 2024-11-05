import asyncio
import os

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')

def webapp_bulider() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Let`s Click!', web_app=WebAppInfo(
            url=URL
        )
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(
        'Hello!',
        reply_markup=webapp_bulider(),
    )

async def main() -> None:
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
