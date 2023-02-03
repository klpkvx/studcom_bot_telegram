from aiogram import types, Dispatcher

import config

from create_bot import dp, bot


async def subs_notify(subs, text, keyboard=None, me=None):
    fails = []
    for chat_id in subs:
        if chat_id != me:
            ret = await bot.send_message(
                chat_id, text, parse_mode='HTML', reply_markup=keyboard)
            if not ret:
                fails.append(str(chat_id))
                if me:
                    await bot.send_message(me, '⚠️ Сообщение {} не доставилось'.format(
                        link('адресату', chat_id)), parse_mode='HTML')
    if len(fails) != 0:
        action_log('Notifying failed for: [{}]'.format(', '.join(fails)))
