import telebot

bot = telebot.TeleBot("1400310128:AAFVC_zZLmjupQEyNK1ZPKrFwnzg-MU4a1E", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Construidme que no se hacer nada")

bot.polling()