import os

MAP_LINK = os.getenv('MAP_LINK')
CONTACTS = os.getenv('CONTACTS')
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set!")
