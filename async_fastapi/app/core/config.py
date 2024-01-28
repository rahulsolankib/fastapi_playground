import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')


settings = Settings()
# in python instead of declaring class var and accessing it with Class.var_name they create object in the very same file and use that variable everywhere.
