import requests
from config import Config


class CompanyAPI:
    """API для работы с компаниями Yougile"""

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS

    def get_companies(self, params=None):
        """Получить список компаний"""
        # Эндпоинт для получения компаний
        url = f"{self.base_url}/api-v2/companies"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def get_company(self, company_id):
        """Получить компанию по ID"""
        url = f"{self.base_url}/api-v2/companies/{company_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def create_company(self, name, description=""):
        """Создать новую компанию"""
        url = f"{self.base_url}/api-v2/companies"
        data = {
            "name": name,
            "description": description
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def edit_company(self, company_id, name, description):
        """Редактировать компанию"""
        url = f"{self.base_url}/api-v2/companies/{company_id}"
        data = {
            "name": name,
            "description": description
        }
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete_company(self, company_id):
        """Удалить компанию"""
        url = f"{self.base_url}/api-v2/companies/{company_id}"
        response = requests.delete(url, headers=self.headers)
        return response

    def set_active_state(self, company_id, is_active):
        """Установить статус активности компании"""
        url = f"{self.base_url}/api-v2/companies/{company_id}/active"
        data = {"is_active": is_active}
        response = requests.patch(url, headers=self.headers, json=data)
        return response
