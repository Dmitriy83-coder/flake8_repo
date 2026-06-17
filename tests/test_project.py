import pytest
from api.project_api import ProjectAPI


class TestProject:
    """Тесты для проектов"""

    @pytest.fixture
    def api(self):
        """Фикстура с API клиентом"""
        return ProjectAPI()

    def test_get_projects(self, api):
        """Тест получения списка проектов"""
        response = api.get_projects()
        assert response.status_code == 200

    def test_create_project_success(self, api):
        """Позитивный тест создания проекта"""
        payload = {
            "title": "ГосУслуги",
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
        }
        response = api.create_project(payload["title"], payload["users"])

        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_missing_title(self, api):
        """Негативный тест создания проекта без названия"""
        payload = {
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
        }
        response = api.request.post("/api-v2/projects", data=payload)

        # Ожидаем ошибку 400
        assert response.status_code == 400

    def test_get_project_by_id(self, api):
        """Тест получения проекта по ID"""
        project_id = "e0ae1650-5860-4fda-815b-cc1cffca176d"
        response = api.get_project(project_id)

        assert response.status_code == 200
        assert "id" in response.json()

    def test_get_nonexistent_project(self, api):
        """Негативный тест получения несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.get_project(fake_id)

        assert response.status_code == 404

    def test_update_project(self, api):
        """Тест обновления проекта"""
        project_id = "e0ae1650-5860-4fda-815b-cc1cffca176d"
        new_title = "Updated Project Title"

        response = api.update_project(project_id, new_title)

        assert response.status_code == 200
        assert response.json()["title"] == new_title
