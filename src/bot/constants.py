import re
from .point_data import POINTS


class Patterns:
    MAIN_MENU = re.compile(r"^main_menu$")
    GET_CONTACTS = re.compile(r"^get_contacts$")
    GET_MAP = re.compile(r"^get_map$")
    SHOW_ROUTE = re.compile(r"^show_route$")
    SHOW_DESC = re.compile(r"^show_desc:(\d+)$")


class ControlTexts:
    WELCOME = "👋 Добро пожаловать!\n\n"
    "Выберите действие из меню ниже 👇"


class ButtonTexts:


    @staticmethod
    def main_menu() -> str:
        return "Главное меню"

    @staticmethod
    def contacts() -> str:
        return "Контакты"

    @staticmethod
    def show_route() -> str:
        return "Посмотреть список интересных объектов\n"

    @staticmethod
    def map() -> str:
        return "Открыть карту"

    @staticmethod
    def short_desc(points_id) -> str:
        return POINTS[points_id]["short_desc"]

    @staticmethod
    def back() -> str:
        return "Вернуться "


class CallbackData:
    START = "start"
    MAIN_MENU = "main_menu"
    CONTACTS = "get_contacts"
    MAP = "get_map"
    SHOW_DESC = "show_desc"
    ROUTE = "show_route"

    @staticmethod
    def show_desc(point_id: str) -> str:
        return f"{CallbackData.SHOW_DESC}:{point_id}"
