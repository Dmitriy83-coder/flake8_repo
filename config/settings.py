import os
from dotenv import load_dotenv

load_dotenv()

class APIConfig:
    BASE_URL = os.getenv("API_BASE_URL", "https://api.poiskkino.dev")
    API_KEY = os.getenv("API_TOKEN", "")  # Это X-API-KEY
    HEADERS = {
        "X-API-KEY": API_KEY,  # ← вместо Authorization: Bearer
        "Content-Type": "application/json"
    }

class UIConfig:
    BASE_URL = os.getenv("UI_BASE_URL", "https://www.kinopoisk.ru")
    LOGIN = os.getenv("UI_LOGIN", "")
    PASSWORD = os.getenv("UI_PASSWORD", "")
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10


class TestData:
    FILM_ID = int(os.getenv("TEST_FILM_ID", 258687))
    FILM_NAME = os.getenv("TEST_FILM_NAME", "Интерстеллар")
    FILM_YEAR = int(os.getenv("TEST_FILM_YEAR", 2014))
    NON_EXISTENT_ID = 999999999
    NON_EXISTENT_YEAR = 2065
