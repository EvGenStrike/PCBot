import telebot
import pcactions
import my_bot_token

bot_path = pcactions.bot_path

token = my_bot_token.bot_token
bot = telebot.TeleBot(token)

file_read = open(rf"{bot_path}\users.txt", "r")
msg_chat_id = file_read.read().strip()
if msg_chat_id != "":
    msg_chat_id = int(msg_chat_id)
    bot.send_message(msg_chat_id,
                     "Компьютер выключается...")
    bot.send_message(msg_chat_id,
                     "Статус бота: offline")
file_read.close()