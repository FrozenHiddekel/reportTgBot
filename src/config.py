from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
