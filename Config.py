import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JMTHON_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JMTHON")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/d1f52c3d109a7462b2497.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
