from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
settings.DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
