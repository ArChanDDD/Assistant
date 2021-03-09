import telebot

bot = telebot.TeleBot('1583853458:AAGKFi8qgnmWNZYrnCBySoTVE51A5lB3KNU')
keyboard_start_tomat = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_start_tomat.row('Начнем!')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, '''
    Привет! 
    Я бот, созданный помочь тебе устроить свое время так, чтобы ты смог работать максимально продуктивно. 
    Пока что я умею только запускать 10-минутные томаты. Попробуем?
    ''', reply_markup=keyboard_start_tomat)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Че это?')


bot.polling(none_stop=True)
