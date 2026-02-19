from decouple import config  # type: ignore


class Config:
    RUN_IN_TERMINAL: bool = config("TERMINAL", default=False)
    "Если указатиь True, то будет запущен в терминале"
    if not RUN_IN_TERMINAL:
        TOKEN: str = config("TOKEN")


config = Config
