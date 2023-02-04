from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token="5713033359:AAEBBgn-55ZDfGVEgLqMTsUmsA3HAjwp5ko")
dp = Dispatcher(bot, storage=storage)
