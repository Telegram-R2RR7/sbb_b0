from dotenv import load_dotenv

load_dotenv()

ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
APP_ID = int(os.environ.get("APP_ID", 6))
API_HASH = os.environ.get("API_HASH") or None
DB_URI = os.environ.get("DATABASE_URL", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN"), None)
