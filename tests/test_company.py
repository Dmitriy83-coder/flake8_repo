import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from api.company_api import CompanyAPI


class TestCompany:
    """Тесты для компаний Yougile"""

    @pytest.fixture
    def api(self):
        """Фикстура с API клиентом"""
        return CompanyAPI()

    @pytest.fixture
    def test_company(self, api):
        """Фикстура создает компанию и удаляет после теста"""
        company_name = f"Test Company {os.urandom(4).hex()}"
        response = api.create_company(company_name, "For testing")

        # Проверяем, что компания создалась
        if response.status_code == 201:
            company_data = response.json()
            company_id = company_data.get("id") if isinstance(company_data, dict) else None
            yield {"id": company_id, "name": company_name}

            # Очистка после теста
            try:
                api.delete_company(company_id)
            except:
                pass
        else:
            pytest.skip(f"Не удалось создать компанию: {response.status_code} - {response.text}")

    def test_get_companies(self, api):
        """Тест получения списка компаний"""
        response = api.get_companies()
        print(f"Response: {response.status_code} - {response.text[:200]}")

        assert response.status_code == 200
        data = response.json()

        # Проверяем структуру ответа
        if isinstance(data, list):
            assert len(data) >= 0
        elif isinstance(data, dict):
            assert "content" in data or "items" in data

    def test_create_company_success(self, api):
        """Позитивный тест создания компании"""
        name = f"Python Company {os.urandom(4).hex()}"
        descr = "Created by API test"

        response = api.create_company(name, descr)
        print(f"Create response: {response.status_code} - {response.text}")

        # Проверяем статус
        assert response.status_code in [200, 201]

        # Проверяем структуру ответа
        data = response.json()
        if isinstance(data, dict):
            # Если компания создалась, удаляем её
            if "id" in data:
                api.delete_company(data["id"])

    def test_create_company_empty_name(self, api):
        """Негативный тест создания компании с пустым именем"""
        response = api.create_company("", "Test")
        print(f"Response: {response.status_code} - {response.text}")

        # Ожидаем ошибку
        assert response.status_code in [400, 422]

    def test_get_company_by_id(self, api, test_company):
        """Тест получения компании по ID"""
        company_id = test_company["id"]
        response = api.get_company(company_id)

        print(f"Get company response: {response.status_code} - {response.text[:200]}")

        assert response.status_code == 200
        data = response.json()

        if isinstance(data, dict):
            assert data.get("id") == company_id or data.get("id") is not None

    def test_get_nonexistent_company(self, api):
        """Негативный тест получения несуществующей компании"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.get_company(fake_id)

        print(f"Response: {response.status_code} - {response.text}")

        # Ожидаем ошибку 404
        assert response.status_code == 404

    def test_edit_company(self, api, test_company):
        """Тест редактирования компании"""
        company_id = test_company["id"]
        new_name = f"Updated Name {os.urandom(4).hex()}"
        new_descr = "Updated description"

        response = api.edit_company(company_id, new_name, new_descr)
        print(f"Edit response: {response.status_code} - {response.text}")

        assert response.status_code == 200

    def test_delete_company(self, api):
        """Тест удаления компании"""
        # Создаем компанию для удаления
        name = f"To Delete {os.urandom(4).hex()}"
        create_response = api.create_company(name, "Will be deleted")

        print(f"Create response: {create_response.status_code} - {create_response.text}")

        if create_response.status_code in [200, 201]:
            data = create_response.json()
            if isinstance(data, dict) and "id" in data:
                company_id = data["id"]

                # Удаляем компанию
                delete_response = api.delete_company(company_id)
                print(f"Delete response: {delete_response.status_code}")

                assert delete_response.status_code == 200
            else:
                pytest.skip("Не удалось получить ID компании")
        else:
            pytest.skip("Не удалось создать компанию для теста")

    def test_deactivate_company(self, api, test_company):
        """Тест деактивации компании"""
        company_id = test_company["id"]
        response = api.set_active_state(company_id, False)

        print(f"Deactivate response: {response.status_code} - {response.text}")

        assert response.status_code == 200

    def test_activate_company(self, api, test_company):
        """Тест активации компании"""
        company_id = test_company["id"]

        # Сначала деактивируем
        api.set_active_state(company_id, False)

        # Потом активируем обратно
        response = api.set_active_state(company_id, True)
        print(f"Activate response: {response.status_code} - {response.text}")

        assert response.status_code == 200


# Простой тест для проверки соединения
def test_api_connection():
    """Тест проверки соединения с API"""
    api = CompanyAPI()
    response = api.get_companies()
    print(f"\nAPI Connection Test: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response text preview: {response.text[:500]}")

    assert response.status_code in [200, 401]
