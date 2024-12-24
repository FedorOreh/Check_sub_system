import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from config import TOKEN, CHANNEL
from aiogram.types import Message
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    result = await bot.get_chat_member(chat_id=CHANNEL, user_id=message.from_user.id)
    if message.chat.type == 'private':
        if result.status != 'left':
            await bot.send_message(message.from_user.id, 'You subbed on channel!')
        else:
            await bot.send_message(message.from_user.id, 'You not subbed. Please sub!',
                                   reply_markup=kb.checking_sub)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

