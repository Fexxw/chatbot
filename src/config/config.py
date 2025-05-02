import os

ENV_BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_TOKEN = "8103234203:AAH-nB2QOC4E-ubMEmYSBxPwFOym4k2YDD0"
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set!")
