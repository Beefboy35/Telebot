import telebot
import config
from advice import *
from telebot import types
import time
bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands=['start'])
def welcome_tothe_club(text):
    sti = open('venv/Images/introimg.jpg', 'rb')
    bot.send_sticker(text.chat.id, sti)
    under_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # under the input-field keyboard
    advice1 = types.KeyboardButton("Sleep")
    advice2 = types.KeyboardButton("Nutrition")
    advice3 = types.KeyboardButton("Workout")
    advice4 = types.KeyboardButton("Mentality")
    under_keyboard.add(advice1, advice2, advice3, advice4)
    bot.send_message(text.chat.id,
                     f"Good ******* time of day <b>{text.from_user.username}</b>! You wanna have some beef on your body? Well im gonna help you! Choose which advice you wanna start with down below!",
                     parse_mode='html', reply_markup=under_keyboard)


# Button press processing
@bot.message_handler(content_types=['text'])
def lala(x):


        if x.text == "Sleep":
            sleep = open("venv/Images/sleep.jpg", "rb")
            bot.send_message(x.chat.id, sleep_advice, parse_mode='html')
            bot.send_sticker(x.chat.id, sleep)
        elif x.text == 'Nutrition':
            nutrition = open("venv/Images/nutrition.jpg", "rb")
            bot.send_message(x.chat.id, nutrition_advice, parse_mode='html')
            bot.send_sticker(x.chat.id, nutrition)
        elif x.text == "Workout":
            workout = open("venv/Images/training.jpg", "rb")
            bot.send_message(x.chat.id, workout_advice, parse_mode='html')
            bot.send_sticker(x.chat.id, workout)
        elif x.text == "Mentality":
            mind1 = open("venv/Images/mentality.jpg", "rb")
            mind2 = open("venv/Images/mindset.jpg", "rb")
            bot.send_message(x.chat.id, mind_advice1, parse_mode='html')
            bot.send_sticker(x.chat.id, mind1)
            time.sleep(10)
            bot.send_message(x.chat.id, mind_advice2, parse_mode='html')
            bot.send_sticker(x.chat.id, mind2)


# @bot.message_handler(content_types=['text'])
# def lala(message):
#     if message.chat.type == 'private':
#         if message.text == "Random Number)":
#             bot.send_message(message.chat.id, str(random.randint(0, 100)))
#         elif message.text == "What is up, bro?":
#             # inline keyboard
#             markup = types.InlineKeyboardMarkup(row_width=8)
#             item1 = types.InlineKeyboardButton("Perfect, gonna go the gym!", callback_data='good')
#             item2 = types.InlineKeyboardButton("It sucks, i torn off my right pec(", callback_data='bad')
#             markup.add(item1, item2)
#             bot.send_message(message.chat.id, 'Im awesome, and you?', reply_markup=markup)
#
#         else:
#             bot.send_message(message.chat.id, 'You are saying bullshit, Speak English, slave!')
#

# Button pressing processing
# @bot.callback_query_handler(func=lambda var: True)
# def callback_inline(var):
#     try:
#         if var.message:
#             if var.data == 'good':
#                 bot.send_message(var.message.chat.id, 'Im glad for you,kid! Keep it up!')
#             elif var.data == 'bad':
#                 bot.send_message(var.message.chat.id, 'Fuck! It does suck, heal your wounds and go back!!')
#
#             # remove inline buttons
#             bot.edit_message_text(chat_id=var.message.chat.id, message_id=var.message.message_id,
#                                   text="What is up, bro?",
#                                   reply_markup=None)
#             # show alert
#             bot.answer_callback_query(callback_query_id=var.message.chat.id, show_alert=True, text="Its just a test!!!")
#
#     except Exception as t:
#         print(repr(t))
#
#
# # RUN
#
#
bot.polling(none_stop=True)
