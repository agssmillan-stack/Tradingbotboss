import telebot

TOKEN = "8360186660:AAGENkMY5jvAjLdmp-tmjcwxllRnZICKytI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu bot de trading en Telegram 🚀")

bot.polling()

