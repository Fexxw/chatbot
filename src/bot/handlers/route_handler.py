from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot import POINTS
from bot.buttons import route_point_button, main_menu_button
from bot.constants import ButtonTexts


async def route_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = []
    back_button = main_menu_button()
    for point in POINTS:
        point_id = point["id"]
        buttons.append(route_point_button(label=point["short"],
                                          point_id=point_id))
    buttons.append(back_button)
    return await update.callback_query.edit_message_text(text=ButtonTexts.show_route(),
                                                         reply_markup=InlineKeyboardMarkup(buttons))
