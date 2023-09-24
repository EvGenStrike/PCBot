import my_bot_token
import telebot
import extensions
import pcactions

token = my_bot_token.bot_token
bot = telebot.TeleBot(token)
msg_chat_id = extensions.read_owner_id()

bot.send_message(msg_chat_id,
                     "Компьютер выключается...")
bot.send_message(msg_chat_id,
                     "Статус бота: offline")
