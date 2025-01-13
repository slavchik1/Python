import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

scores = {}

choices = ["Камінь", "Ножиті", "Папір"]

@bot.message_handler(command=["start"])
def start(message):
    user_id = message.from_user.id
    scores[user_id] = {"user": 0, "bot": 0}

    bot.send_message(message.chat.id, "Гра запущена.")

bot.polling(non_stop=True)
