from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types, Dispatcher
from create_bot import dp

from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    room_number = State()
    build = State()

# Начало диалога для инициализации пользователя


# @dp.message_handler(commands='load', state=None)
async def init_data(message: types.Message, state: FSMContext, commands='load'):
    await FSMAdmin.room_number.set()
    await message.reply('Отменить ввод: /end\nВведи номер своей комнаты:')


# @dp.message_handler(state=FSMAdmin.room_number)
async def init_room_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['room_number'] = (int)(message.text)
    await FSMAdmin.next()
    await message.reply('Введи свой корпус:')


# @dp.message_handler(state=FSMAdmin.build)
async def init_build(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['build'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


# Выход из состояний модуля
@dp.message_handler(state="*", commands='end')
@dp.message_handler(Text(equals='end', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ввод был успешно отменен')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(init_data, state=None, commands=['load'])
    dp.register_message_handler(init_room_number, state=FSMAdmin.room_number)
    dp.register_message_handler(init_build, state=FSMAdmin.build)
    dp.register_message_handler(cancel_handler, state="*", commands=['end'])
    dp.register_message_handler(cancel_handler, Text(
        equals='end', ignore_case=True), state="*")
