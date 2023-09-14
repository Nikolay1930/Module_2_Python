import requests
from bs4 import BeautifulSoup
import random
import telebot
from DS.settings_bot import *  # не пишите это!!!!!!!!!!!!
# token = '50054646446:smfmskfksjkjvxokscslcsclsclscls'     # а эту пишите!!!!!!!!!!!!

bot = telebot.TeleBot(token)


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='p-2 clearfix'))
    return [res.text, res.a.attrs['href']]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_txt = '''Добро пожаловать!'''
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Случайная картинка')
    button3 = telebot.types.KeyboardButton('Кнопка 3')
    button4 = telebot.types.KeyboardButton('Стикер')
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome_txt, reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    text = get_fact()
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_in = telebot.types.InlineKeyboardButton('Перейти...', url=text[1])
    keyboard.add(button_in)
    bot.send_message(message.chat.id, text[0], reply_markup=keyboard)
    # bot.send_message(message.chat.id, text[1])


@bot.message_handler(commands=['img'])
def send_img(message):
    # number_img = random.randint(1, 3)
    # # img = open(str(number_img) + '_send_photo.png', 'rb')
    # img = open(f'{number_img}_send_photo.png', 'rb')
    name_random_img = random.choice(['1_send_photo.png', '2_send_photo.png', '3_send_photo.png'])
    img = open(name_random_img, 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(content_types='text')
def message_reply(message):
    if 'аудио' in message.text.lower():
        song = open('audio.mp3', 'rb')
        bot.send_audio(message.chat.id, song)
    elif 'факт' in message.text.lower():
        send_fact(message)
    elif 'Случайная картинка' == message.text:
        send_img(message)
    elif 'Кнопка 3' == message.text:
        bot.send_message(message.chat.id, 'Ты нажал на кнопку 3!')
    elif 'Стикер' == message.text:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG7lZjoycd83uFPwW_QCwPlSGnZ0ojLQACLQwAAkKvaQABylqlGZsif0csBA')
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()