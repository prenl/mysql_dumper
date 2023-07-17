from dotenv import load_dotenv
from os import environ

load_dotenv()

DB_HOST = environ.get("DB_HOST")
DB_NAME = environ.get("DB_NAME")
DB_USER = environ.get("DB_USER")
DB_PASSWORD = environ.get("DB_PASSWORD")

DIRECTORY = environ.get("DIRECTORY")
TIMEOUT = int(environ.get("TIMEOUT"))
MAX_DAYS = int(environ.get("MAX_DAYS"))
DATE_FORMAT = environ.get("DATE_FORMAT")
