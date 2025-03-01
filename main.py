from config import dp, Admins, bot
import logging
from aiogram import executor
from handlers import (commands, store_fsm, send_products, storeforall)
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!')


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')
        

commands.register_handlers(dp)
store_fsm.register_handlers_store(dp)
send_products.register_handlers(dp)
storeforall.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)