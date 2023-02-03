from utils import client, admin, other
from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):  # info about start bot
    print('Bot has been started\n')


'''Client_part'''


client.register_handlers_client(dp)
other.register_handlers_toher(dp)

'''Common part'''


# Самый последний Хендлер в который все говно будет попадать

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
