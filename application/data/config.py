import os

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = str(os.getenv("SECRET_KEY"))
APPID = str(os.getenv("APPID"))

WTF_CSRF_ENABLED = True


class Configuration(object):
    DEBUG = True