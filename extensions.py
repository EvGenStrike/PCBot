import my_bot_token
import telebot
import pcactions

token = my_bot_token.bot_token
bot = telebot.TeleBot(token)
bot_path = pcactions.bot_path

def read_owner_id():
    file_read = open(rf"{bot_path}\users.txt", "r")
    msg_chat_id = file_read.read().strip()
    file_read.close()
    if msg_chat_id != "":
        return int(msg_chat_id)
    return None

