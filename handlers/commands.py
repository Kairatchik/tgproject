# commands.py
from aiogram import types, Dispatcher
from config import bot



async def start_handler(message: types.Message):
    print('Обработчик старта')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram ID - {message.from_user.id}\n')

    await message.answer('Привет мир')

async def start_info(message: types.Message):
    print('Обработчик /info')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'🛍 Добро пожаловать в наш магазин-бот!\n\n'
                                f'📌 Здесь вы можете:\n'
                                f'🔹 Просматривать каталог товаров\n'
                                f'🔹 Оформлять заказы прямо в боте\n'
                                f'🔹 Выбирать удобный способ оплаты\n'
                                f'🔹 Получать быструю поддержку\n\n'
                                f'💳 Доступные способы оплаты:\n'
                                f'- Банковские карты\n'
                                f'- Электронные кошельки\n'
                                f'- Криптовалюта (если поддерживается)\n\n'
                                f'📦 Доставка:\n'
                                f'🚀 Быстрая отправка по всей стране!\n\n'
                                f'❓ Если у вас есть вопросы, пишите: @support_username\n\n'
                                f'💬 Для оформления заказа используйте команду /order')




def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(start_info, commands=['info'])
