import telebot
import time
import funcs

tomato_time = 1
waiting_count = False
data_list = []

bot = telebot.TeleBot('1583853458:AAGKFi8qgnmWNZYrnCBySoTVE51A5lB3KNU')
keyboard_start_tomat = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_start_tomat.row('Начнем!')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, '''
    Привет! 
    Я бот, созданный помочь тебе устроить свое время так, чтобы ты смог работать максимально продуктивно. 
    Пока что я умею только запускать 10-минутные томаты. Попробуем?
    P.S. давай считать, что ты книжку читаешь :)
    ''', reply_markup=keyboard_start_tomat)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    if message.text.isdigit():
        data_list.append(int(message.text))
        bot.send_message(message.chat.id, 'Отлично! Пока что отдохни, а меня сделают чуть умнее, и я вернусь!')
    elif message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text == 'Начнем!':
        bot.send_message(message.from_user.id, 'Начали!')
        funcs.start_printed_timer(bot, message, tomato_time * 60, chat_id)
        bot.send_message(message.from_user.id, 'Сколько ты успел прочитать страниц?')
    else:
        bot.send_message(message.from_user.id, 'Че это?')


bot.polling(none_stop=True)
