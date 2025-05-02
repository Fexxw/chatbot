from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from bot.buttons import ButtonTexts
from bot.constants import CallbackData


from bot.buttons import route_menu_button, map_button, contacts_button


async def main_menu_handler(update: Update, context: CallbackContext):
    buttons = InlineKeyboardMarkup([
        route_menu_button(),
        map_button(),
        contacts_button(),
    ])

    if update.message:
        await update.message.reply_text(ButtonTexts.main_menu(), reply_markup=buttons)
    elif update.callback_query:
        await update.callback_query.edit_message_text(ButtonTexts.main_menu(), reply_markup=buttons)
