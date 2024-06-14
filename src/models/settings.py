from pydantic import SecretStr, HttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

  debug: bool = False
  
  grpc_host: str
  grpc_port: int
  topic: str
  password: SecretStr
  user: str
  url: HttpUrl
  api_version: str = "57.0"
