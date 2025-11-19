import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Récupération du token sécurisé depuis Render
JETON = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(JETON)

# -----------------------
# MESSAGE D’ACCUEIL
# -----------------------
MESSAGE_BIENVENUE = (
    "👋 Bonjour et bienvenue dans la *Formation Shopify Afrique !*\n\n"
    "Je suis l’assistante *Coach Shopify Pro™*.\n"
    "Pose-moi tes questions, je suis là pour t’aider à réussir 🔥🚀"
)

@bot.message_handler(commands=['start'])
def accueil(message):
    bot.reply_to(message, MESSAGE_BIENVENUE)

@bot.message_handler(func=lambda msg: True)
def reponse_auto(message):
    bot.reply_to(message, "💬 Message bien reçu, l’assistante te répond !")

# Lancement du bot
bot.polling(none_stop=True)
