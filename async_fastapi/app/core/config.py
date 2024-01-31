import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(dotenv_path='.envrc')


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv('SQLALCHEMY_DATABASE_URL')


settings = Settings()
# in python instead of declaring class var and accessing it with Class.var_name they create object in the very same file and use that variable everywhere.
