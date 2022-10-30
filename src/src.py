#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import telebot
from telebot import types


# In[ ]:


bot = telebot.TeleBot('5590721685:AAHnMN0qvgCJuJhhUtzQ2wRsZH4i2vZts_E')


# In[ ]:


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ДСЛ")
    btn2 = types.KeyboardButton("ДС")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери общежитие, в котором ты живёшь".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.chat.type == "private":
        if (message.text == "ДСЛ"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("ДСЛ А")
            btn4 = types.KeyboardButton("ДСЛ Б")
            markup.add(btn3, btn4)
            bot.send_message(message.chat.id, text="Выбери корпус".format(message.from_user), reply_markup=markup)
        if(message.text == "ДСЛ А"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn12 = types.KeyboardButton("А9")
            btn13 = types.KeyboardButton("А10")
            btn14 = types.KeyboardButton('А11')
            btn15 = types.KeyboardButton('А12')
            markup.add(btn12, btn13, btn14, btn15)
            bot.send_message(message.chat.id, text="Выбери этаж".format(message.from_user), reply_markup=markup)
        if(message.text == "ДСЛ Б"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn16 = types.KeyboardButton("ДСЛ Б8")
            btn17 = types.KeyboardButton("ДСЛ Б9")
            btn18 = types.KeyboardButton('ДСЛ Б10')
            markup.add(btn16, btn17, btn18)
            bot.send_message(message.chat.id, text="Выбери этаж".format(message.from_user), reply_markup=markup)
        if(message.text == "А9"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Караваева Александра. По всем возникшим вопросам можешь написать ей, ссылка на её профиль в вк: vk.com/alexandra_karavaeva".format(message.from_user))
        if(message.text == "А10"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Гладышева Виктория. По всем возникшим вопросам можешь написать ей, ссылка на её профиль в вк: vk.com/sertraline_diet".format(message.from_user))
        if(message.text == "А11"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Шипицын Матвей. По всем возникшим вопросам можешь написать ему, ссылка на его профиль в вк: vk.com/id190431554".format(message.from_user))
        if(message.text == "А12"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Микляева Дарья. По всем возникшим вопросам можешь написать ей, ссылка на её профиль в вк: vk.com/mikl26".format(message.from_user))
        if(message.text == "ДСЛ Б8"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Зарбактаев Гарма. По всем возникшим вопросам можешь написать ему, ссылка на его профиль в вк: vk.com/garma_zarbaktaev".format(message.from_user))
        if(message.text == "ДСЛ Б9"):
            bot.send_message(message.chat.id, text="Тебе повезло: у тебя целых две старосты этажа! \n \nА именно: Гладышева Виктория (ссылка на её профиль в вк: vk.com/sertraline_diet) и Циберева Елизавета (ссылка на её профиль в вк: vk.com/el.tsbrv). \n \nПо всем возникающим вопросам ты можешь обращаться к ним.".format(message.from_user))
        if(message.text == "ДСЛ Б10"):
            bot.send_message(message.chat.id, text="Староста твоего этажа - Долгих Елизавета. По всем возникшим вопросам можешь написать ей, ссылка на её профиль в вк: vk.com/lisa_dol".format(message.from_user))
        if(message.text == 'ДС'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn6 = types.KeyboardButton("ДС Б")
            btn7 = types.KeyboardButton("ДС Г")
            btn8 = types.KeyboardButton('ДС Д')
            btn9 = types.KeyboardButton("ДС Е")
            btn10 = types.KeyboardButton("ДС Ж")
            markup.add(btn6, btn7, btn8, btn9, btn10)
            bot.send_message(message.chat.id, text="Выбери корпус".format(message.from_user), reply_markup=markup)
        if(message.text == "ДС Б"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn12 = types.KeyboardButton("3-7")
            btn13 = types.KeyboardButton("8-10")
            btn17 = types.KeyboardButton("11-13")
            btn14 = types.KeyboardButton('14')
            btn15 = types.KeyboardButton('15')
            btn16 = types.KeyboardButton('20-23')
            markup.add(btn12, btn13, btn17, btn14, btn15, btn16)
            bot.send_message(message.chat.id, text="Выбери свой этаж".format(message.from_user), reply_markup=markup)
        if(message.text == "3-7"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Арина Сиухина (vk.com/id_arinka.balerinka) и Мария Маркова (vk.com/m_mar). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "8-10"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Светлана Матуз (vk.com/svetlana_matuz) и Владислав Муджиков (vk.com/vladkier). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "11-13"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Александра Архипова (vk.com/toosasshaforyou) и Алина Арсланова (vk.com/alinaarslnva). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "14"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Давид Габидуллин (vk.com/davidspace), Анна Павликова (vk.com/malinoviparket) и Гриненко Алексей (vk.com/grintus). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "15"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Аделина Мамлеева (vk.com/adelinexbx), Елизавета Тюнина (vk.com/vasilyocheck) и Черников Иван (vk.com/id60826450). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == '20-23'):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Вячеслав Чуб (vk.com/kryakva_vub) и Екатерина Агуреева (vk.com/katangenc). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "ДС Г"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn12 = types.KeyboardButton("1-4")
            btn13 = types.KeyboardButton("5-9")
            markup.add(btn12, btn13)
            bot.send_message(message.chat.id, text="Выбери свой этаж".format(message.from_user), reply_markup=markup)
        if(message.text == "1-4"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Илья Бардамов (vk.com/ilyab171) и Александр Каблин (vk.com/id_alejandr0). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "5-9"):
            bot.send_message(message.chat.id, text="Старосты твоего этажа - Степан Павленко (vk.com/stepan.pavlenko) и Арсений Трубицин (vk.com/a.trubitsin2013). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "ДС Д"):
            bot.send_message(message.chat.id, text="Старосты твоего корпуса - Рамазан Гедиев (vk.com/liberahasosat) и Дмитрий Петровский (vk.com/imfuckingbitch). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "ДС Е"):
            bot.send_message(message.chat.id, text="Старосты твоего корпуса - Илья Бардамов (vk.com/ilyab171) и Александр Каблин (vk.com/id_alejandr0). По всем возникшим вопросам можешь написать им.".format(message.from_user))
        if(message.text == "ДС Ж"):
            bot.send_message(message.chat.id, text="Старосты твоего корпуса - Алексей Горьков (vk.com/letsgoantoxa) и Иван Васильев (vk.com/doublerainbow2002). По всем возникшим вопросам можешь написать им.".format(message.from_user))


# In[ ]:


bot.polling(none_stop=True, interval=0)


# In[ ]:



