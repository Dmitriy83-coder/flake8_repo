class Project:
    """Модель проекта"""

    def __init__(self, title, users=None, is_active=True):
        self.title = title
        self.users = users or {}
        self.is_active = is_active
        self.id = None

    def to_dict(self):
        """Преобразовать в словарь для API"""
        return {
            "title": self.title,
            "users": self.users,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):
        """Создать из словаря от API"""
        project = cls(
            title=data.get("title", ""),
            users=data.get("users", {}),
            is_active=data.get("is_active", True)
        )
        project.id = data.get("id")
        return project
