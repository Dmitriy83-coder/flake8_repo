import requests
from config import Config

BASE_URL = "https://ru.yougile.com"

API_KEY = "0AEicH5mPQ3V29BCvS7AgnRNATRM1WV8jd9gxCUKxnXOcEaS7-Fn7-RKUFuYjymx"

PROJECT_ID = "b9a046c6-7c1d-496d-a751-f0b68220de0c"


def test_api_key_auth():
    """Тест авторизации по API ключу"""
    headers = {
        "Authorization": f"Bearer {Config.API_KEY}"
    }
    response = requests.get(f"{Config.BASE_URL}/api-v2/projects", headers=headers)

    # Если ключ валидный - статус 200
    # Если невалидный - 401
    assert response.status_code in [200, 401]

    if response.status_code == 200:
        print("✅ API ключ валидный")
    else:
        print("❌ API ключ невалидный")


def test_simple_request():
    """Простой запрос для проверки соединения"""
    response = requests.get(f"{Config.BASE_URL}/api-v2/projects")
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        print("✅ Соединение с API установлено")
    else:
        print(f"❌ Ошибка соединения: {response.status_code}")
