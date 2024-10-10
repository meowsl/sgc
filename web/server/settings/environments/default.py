from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv("DEBUG", True)
SITE_DOMAIN = os.getenv("SITE_DOMAIN")
BASE_URL = os.getenv("BASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)
REFRESH_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 720)
)

USE_SQLITE = os.getenv("USE_SQLITE", True)
DATABASE_URL = os.getenv("DATABASE_URL")

ORIGINS = [
    "*"
] if SITE_DOMAIN == "*" else [str(SITE_DOMAIN)]
