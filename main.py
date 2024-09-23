import telebot
import config
from advice import *
from telebot import types
import time

bot = telebot.TeleBot(config.TOKEN)


# Quite a simple telegram bot that gives some advice on how to get in shape and so on
# Token is located in the config.py module
# Tips are in the advice.py module
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


if __name__ == "__main__":
    try:
        print("The bot is running successfully")
        bot.polling(none_stop=True)

    except Exception as er:
        print(er)

    else:
        print("The bot has just been terminated with the exit code 0")

