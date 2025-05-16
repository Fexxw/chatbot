from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from bot.constants import *
from bot.handlers import *
from config.config import BOT_TOKEN


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    handlers = [CommandHandler("start", start_handler),
                CallbackQueryHandler(main_menu_handler, pattern=Patterns.MAIN_MENU),
                CallbackQueryHandler(get_contacts_handler, pattern=Patterns.GET_CONTACTS),
                CallbackQueryHandler(get_map_handler, pattern=Patterns.GET_MAP),
                CallbackQueryHandler(expand_point_handler, pattern=Patterns.SHOW_DESC),
                CallbackQueryHandler(route_handler, pattern=Patterns.SHOW_ROUTE)]
    app.add_handlers(handlers)

    app.run_polling()


if __name__ == "__main__":
    main()
