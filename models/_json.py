import json
from pathlib import Path


class JSONHelper:
    """Класс для работы с JSON файлами"""

    @staticmethod
    def save_to_file(data, filename):
        """Сохранить данные в JSON файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_file(filename):
        """Загрузить данные из JSON файла"""
        if not Path(filename).exists():
            return None
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_test_data(company_id, filename="test_data.json"):
        """Сохранить ID созданной компании для отладки"""
        data = JSONHelper.load_from_file(filename) or {}
        data["last_company_id"] = company_id
        JSONHelper.save_to_file(data, filename)

    @staticmethod
    def get_last_company_id(filename="test_data.json"):
        """Получить последний ID компании"""
        data = JSONHelper.load_from_file(filename) or {}
        return data.get("last_company_id")
