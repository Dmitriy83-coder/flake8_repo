import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)


class Config:
    """Конфигурация для тестов"""

    BASE_URL = os.getenv("BASE_URL", "https://ru.yougile.com")
    API_KEY = os.getenv("API_KEY")
    PROJECT_ID = os.getenv("PROJECT_ID")

    # Заголовки для API запросов
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Проверка наличия API ключа
    if not API_KEY:
        print("⚠️ ВНИМАНИЕ: API_KEY не найден в .env файле!")
