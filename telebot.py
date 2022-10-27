from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

"""
pip install python-telegram-bot

Get chat-id for simpleRestTelebot.py
Type /start in chat and then execute this script,
it will return the chatId in the telegram chat with your bot.
"""

updater = Updater("API-KEY", use_context=True)
def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"{update.message.chat_id}")
  