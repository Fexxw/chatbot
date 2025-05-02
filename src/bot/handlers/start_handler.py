from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from .main_menu_handler import main_menu_handler
from bot.buttons import ControlTexts


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ControlTexts.WELCOME)
    return await main_menu_handler(update, context)
