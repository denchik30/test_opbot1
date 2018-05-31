import telebot


TOKEN = '527221399:AAGbt7upt7Y82EyXwPgZiyP1xZYkjQVkKr0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
