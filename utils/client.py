from aiogram import types, Dispatcher


from create_bot import dp, bot

# @dp.message_handler(commands=['start'])


async def commands_start(message: types.Message):
    if (message.text == '/start'):
        await bot.send_message(message.from_user.id, "HERE WILL BE INFO ABOUT BOT")


# @dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):
    if (message.text == '/help'):
        await bot.send_message(message.from_user.id, "— Команды бота\n🕰 Время работы: \n• /day — сколько отработано за день\n• /week — сколько отработано за неделю")


# @dp.message_handler(commands=['wash_clothes'])
async def commands_wash_clothes(message: types.Message):
    await bot.send_dice(message.from_user.id)
    await bot.send_message(message.from_user.id, "График работы постирочной:")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_help, commands=['help'])
    dp.register_message_handler(
        commands_wash_clothes, commands=['wash_clothes'])
