import os

from dotenv import load_dotenv

load_dotenv()

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PASSWORD = os.getenv("PASSWORD")
MSG_START = os.getenv("MSG_START")
MSG_ORGAO = os.getenv("MSG_ORGAO")
MSG_SENHA = os.getenv("MSG_SENHA")
MSG_SENHA_NOK = os.getenv("MSG_SENHA_NOK")
MSG_TITULO = os.getenv("MSG_TITULO")
MSG_CARGO = os.getenv("MSG_CARGO")
MSG_DDD = os.getenv("MSG_DDD")
MSG_TEL = os.getenv("MSG_TEL")
MSG_LOG = os.getenv("MSG_LOG")