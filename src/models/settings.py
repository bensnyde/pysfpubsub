from pydantic import SecretStr, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DEBUG: bool = True
    GRPC_HOST: str
    GRPC_PORT: int
    TOPIC: str
    PASSWORD: SecretStr
    USER: str
    URL: HttpUrl
    API_VERSION: str = "57.0"
