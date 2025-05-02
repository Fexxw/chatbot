import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from bot.buttons import main_menu_button


async def get_map_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    map_url = os.environ.get("MAP_LINK")

    await update.callback_query.edit_message_text(
        f"Map of the apartments: {map_url}",
        reply_markup=InlineKeyboardMarkup([main_menu_button()])
    )
