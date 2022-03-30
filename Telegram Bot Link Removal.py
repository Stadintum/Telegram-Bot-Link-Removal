import telebot
from time import time

#TOKEN
bot = telebot.TeleBot("5189824609:AAHtGBj-0QXDNOUDhgK4R7IjZkhIz0jlOhs")

# ID вашей группы
GROUP_ID = -1001536932462

# Удаляем сообщения с ссылкой
@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return


if __name__ == "__main__":
    bot.infinity_polling()