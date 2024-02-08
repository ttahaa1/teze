from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6264668799"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/81d5881f45404a436dd55.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/81d5881f45404a436dd55.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ZERO_R7K")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZERO_R7K")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6264668799").split()))


FAILED = "https://telegra.ph/file/81d5881f45404a436dd55.jpg"
