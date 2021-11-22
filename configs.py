from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    API_ID = int(getenv("API_ID", "6435225"))
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    SESSION = getenv("SESSION", "session")
    OWNER_ID = int(getenv("OWNER_ID", "1669178360"))
    SUPPORT = getenv("SUPPORT", "https://t.me/Superior_support")
    CHANNEL = getenv("CHANNEL", "https://t.me/Superior_bots")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/itsunknown-12")


config = Config()
