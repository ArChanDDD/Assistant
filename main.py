import telebot

bot = telebot.TeleBot('1583853458:AAGKFi8qgnmWNZYrnCBySoTVE51A5lB3KNU')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Shalom')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Че это?')


bot.polling(none_stop=True)
