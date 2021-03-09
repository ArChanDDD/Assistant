import time


def start_printed_timer(bot, message, time_in_seconds, chat_id):
    mes_id = bot.send_message(message.chat.id,
                              "Отсчет времени: {0}:{1}".format(time_in_seconds // 60 % 60, time_in_seconds % 60)).message_id
    time_in_seconds -= 1
    while time_in_seconds >= 0:
        bot.edit_message_text("Отсчет времени: {0}:{1}".format(time_in_seconds // 60 % 60, time_in_seconds % 60),
                              message_id=mes_id, chat_id=chat_id)
        time_in_seconds -= 1
        time.sleep(1)
