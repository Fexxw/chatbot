from telegram import Update
from telegram.ext import ContextTypes

from bot.buttons import ControlTexts
from .main_menu_handler import main_menu_handler


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ControlTexts.WELCOME)
    return await main_menu_handler(update, context)
