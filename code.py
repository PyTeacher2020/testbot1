import telebot
import parser

#main variables
TOKEN = "1163060645:AAFJCM4Ud8ytSwYAjQVi4TS8Oi04hBMbxp4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()
