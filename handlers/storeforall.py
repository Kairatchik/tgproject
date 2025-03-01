from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import buttons


class OrderFSM(StatesGroup):
    article = State()
    size = State()
    quantity = State()
    contact = State()
    submit = State()


async def start_fsm_order(message: types.Message):
    await message.answer('Введите артикул товара:', reply_markup=buttons.cancel_fsm)
    await OrderFSM.article.set()

async def article_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text
    
    await OrderFSM.next()
    await message.answer('Введите размер товара:')

async def size_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    
    await OrderFSM.next()
    await message.answer('Введите количество товара:')

async def quantity_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    
    await OrderFSM.next()
    await message.answer('Введите ваш номер телефона:')

async def contact_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
    
    await OrderFSM.next()
    await message.answer(f'Проверьте данные:
Артикул: {data["article"]}
Размер: {data["size"]}
Количество: {data["quantity"]}
Контактные данные: {data["contact"]}', reply_markup=buttons.submit)

async def submit_load(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            # Здесь можно добавить сохранение данных в базу
            await message.answer('Ваш заказ сохранен!', reply_markup=buttons.remove_keyboard)
            await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()
    else:
        await message.answer('Выберите "да" или "нет".')


def register_handlers_order(dp: Dispatcher):
    dp.register_message_handler(start_fsm_order, commands=['order'])
    dp.register_message_handler(article_load, state=OrderFSM.article)
    dp.register_message_handler(size_load, state=OrderFSM.size)
    dp.register_message_handler(quantity_load, state=OrderFSM.quantity)
    dp.register_message_handler(contact_load, state=OrderFSM.contact)
    dp.register_message_handler(submit_load, state=OrderFSM.submit)