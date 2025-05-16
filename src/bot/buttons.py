from telegram import InlineKeyboardButton

from .constants import *


def welcome_button():
    return [InlineKeyboardButton(ControlTexts.WELCOME, callback_data=CallbackData.START)]


def main_menu_button():
    return [InlineKeyboardButton(ButtonTexts.main_menu(), callback_data=CallbackData.MAIN_MENU)]


def contacts_button():
    return [InlineKeyboardButton(ButtonTexts.contacts(), callback_data=CallbackData.CONTACTS)]


def map_button():
    return [InlineKeyboardButton(ButtonTexts.map(), callback_data=CallbackData.MAP)]


def route_menu_button():
    return [InlineKeyboardButton(ButtonTexts.show_route(), callback_data=CallbackData.ROUTE)]


def route_point_button(point_id: str, label: str):
    return [InlineKeyboardButton(label, callback_data=CallbackData.show_desc(point_id))]

