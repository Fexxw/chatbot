from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot import POINTS
from bot.buttons import route_menu_button


async def expand_point_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, point_id = query.data.split(":")

    point_id = int(point_id)
    point = POINTS[point_id - 1]

    await query.edit_message_text(
        f"*{point_id}. {point['short']}*\n\n{point['long']}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([route_menu_button()])
    )
