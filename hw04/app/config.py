from os import environ
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_HOST: str = environ.get('DB_HOST', 'localhost')
    DB_PORT: int = environ.get('DB_PORT', '5432')
    DB_NAME: str = environ.get('DB_NAME', 'postgres')
    DB_USER: str = environ.get('DB_USER', 'postgres')
    DB_PASSWORD: str = environ.get('DB_PASSWORD', 'pgpass')

    model_config = SettingsConfigDict()


settings = Settings()
