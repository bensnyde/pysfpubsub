import logging
from settings import Settings


def run(settings: Settings) -> None:
  raise NotImplementedError

if __name__ == '__main__':
  settings = Settings()
  logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO
  )
