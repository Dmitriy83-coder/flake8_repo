from api.request import Request
from config import Config


class ProjectAPI:
    """API для работы с проектами"""

    def __init__(self):
        self.request = Request()
        self.project_id = Config.PROJECT_ID

    def get_projects(self):
        """Получить список проектов"""
        response = self.request.get("/api-v2/projects")
        return response

    def get_project(self, project_id):
        """Получить проект по ID"""
        response = self.request.get(f"/api-v2/projects/{project_id}")
        return response

    def create_project(self, title, users=None):
        """Создать новый проект"""
        data = {
            "title": title,
            "users": users or {}
        }
        response = self.request.post("/api-v2/projects", data=data)
        return response

    def update_project(self, project_id, title, users=None):
        """Обновить проект"""
        data = {
            "title": title,
            "users": users or {}
        }
        response = self.request.put(f"/api-v2/projects/{project_id}", data=data)
        return response

    def delete_project(self, project_id):
        """Удалить проект"""
        response = self.request.delete(f"/api-v2/projects/{project_id}")
        return response

    def deactivate_project(self, project_id):
        """Деактивировать проект"""
        data = {"is_active": False}
        response = self.request.patch(f"/api-v2/projects/{project_id}", data=data)
        return response
