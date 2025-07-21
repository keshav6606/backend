import json
from os import getenv, path
from dotenv import load_dotenv
from Backend import LOGGER


load_dotenv(path.join(path.dirname(path.dirname(__file__)), "config.env"))
class Telegram:
    API_ID = int(getenv("API_ID", "26954495"))
    API_HASH = getenv("API_HASH", "2061c55207cfee4f106ff0dc331fe3d9")
    BOT_TOKEN = getenv("BOT_TOKEN", "7594581650:AAE5IIr5Yw8QhCUqe9B3dYgSzLqhDwzJMGU")
    PORT = int(getenv("PORT", "8000"))
    BASE_URL = getenv("BASE_URL", "0.0.0.0").rstrip('/')
    AUTH_CHANNEL = [channel.strip() for channel in (getenv("AUTH_CHANNEL") or "").split(",") if channel.strip()]
    DATABASE = getenv("DATABASE", "mongodb+srv://cinemahub940:cinemahub940@cluster0.hmz84fc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").split(", ")
    TMDB_API = getenv("TMDB_API", "6abcb6bb99fb77f33c37016a28866ed2")
    IMDB_API = getenv("IMDB_API", "6abcb6bb99fb77f33c37016a28866ed2")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
    MULTI_CLIENT = getenv("MULTI_CLIENT", "true").lower() == "true"
    USE_CAPTION = getenv("USE_CAPTION", "False").lower() == "true"
    USE_TMDB = getenv("USE_TMDB", "False").lower() == "true"
    OWNER_ID = int(getenv("OWNER_ID", "7045947967"))
    USE_DEFAULT_ID = getenv("USE_DEFAULT_ID", None)
