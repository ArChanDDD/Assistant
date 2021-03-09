import telebot
import time

bot = telebot.TeleBot('1583853458:AAGKFi8qgnmWNZYrnCBySoTVE51A5lB3KNU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Привет! Я бот, созданный помочь тебе устроить свое время так, чтобы ты смог 
    работать максимально продуктивно. Пока что я умею только запускать 10-минутные томаты. Попробуем?''')
    bot.send_message(message.chat.id, 'Будет весело!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Че это?')


bot.polling(none_stop=True)
