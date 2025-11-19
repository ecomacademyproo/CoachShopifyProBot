import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# ————————————
# MESSAGE D’ACCUEIL
# ————————————

WELCOME_MESSAGE = """
👋 *Bienvenue dans la formation Shopify Afrique !*
Je suis l’assistante *Coach Shopify Pro™*.

✔ *Formation 100% gratuite*  
✔ *Boutique clé en main*  
✔ *Gagne jusqu’à 500.000 FCFA/jour*  

👉 Clique sur *CONTINUER* ci-dessous pour rejoindre le canal officiel.
"""

CHANNEL_LINK = "https://t.me/CoachShopifyProAfrique"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("➡️ CONTINUER", url=CHANNEL_LINK)
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        WELCOME_MESSAGE,
        parse_mode="Markdown",
        reply_markup=markup
    )

print("Bot lancé...")
bot.polling()
