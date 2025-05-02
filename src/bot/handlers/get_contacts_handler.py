import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes


from bot.buttons import main_menu_button
from bot.constants import ButtonTexts


async def get_contacts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contacts = os.environ.get("CONTACTS")

    await update.callback_query.edit_message_text(
        f"Contacts: {contacts}",
        reply_markup=InlineKeyboardMarkup([main_menu_button()])
    )
