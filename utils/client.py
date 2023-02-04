from aiogram import types, Dispatcher

import config

from create_bot import dp, bot
from utils.common_utils import subs_notify

# @dp.message_handler(commands=['start'])


# приветственное сообщение при /start
async def commands_start(message: types.Message):
    if (message.text == '/start'):
        with open(config.FileLocation.cmd_start, 'r', encoding='utf-8') as file:
            await bot.send_message(message.from_user.id, file.read(), parse_mode=types.ParseMode.HTML)


 # описание функционала бота /help
# @dp.message_handler(commands=['help']


async def commands_help(message: types.Message):
    '''cmd_help_file = open(config.FileLocation.cmd_help, 'r', encoding='utf-8')
    string = ""
    for line in cmd_help_file:
        string = string + line
    await bot.send_message(message.from_user.id, string, parse_mode=types.ParseMode.HTML)'''
    with open(config.FileLocation.cmd_help, 'r', encoding='utf-8') as file:
        await bot.send_message(message.from_user.id, file.read(), parse_mode=types.ParseMode.HTML)


# график работы постирочной /wash_clothes
# @dp.message_handler(commands=['wash_clothes'])
async def commands_wash_clothes(message: types.Message):
    await bot.send_dice(message.from_user.id)
    await bot.send_message(message.from_user.id, "График работы постирочной:")


# обмен белья  /exchange_linen
async def commands_exchange_linen(message: types.Message):
    await bot.send_message(message.from_user.id, "В такие-то дни обмен белья:")


async def commands_feedback(message: types.Message):
    split = message.text.split(' ', 1)
    if len(split) > 1:
        await subs_notify(config.admin_ids,
                          'Обратная связь от \n@{}\n{}:\n{}'.format(message.from_user.username, message.from_user.full_name, split[1]))
        await bot.send_message(message.from_user.id, "Фидбек отправлен!")
    else:
        await bot.send_message(message.from_user.id, "/feedback [ваше обращение]")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])  # /start
    dp.register_message_handler(commands_help, commands=['help'])  # /help
    dp.register_message_handler(
        commands_wash_clothes, commands=['wash_clothes'])  # /wash_clothes
    dp.register_message_handler(
        commands_exchange_linen, commands=['exchange_linen'])  # exchange_linen
    dp.register_message_handler(commands_feedback, commands=['feedback'])
