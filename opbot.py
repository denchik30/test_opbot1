import telebot


TOKEN = '527221399:AAGbt7'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.sent_message(message.chat.id, 'Привет! Как дела?')

bot.polling()
