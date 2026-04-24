class Company:
    """Модель компании"""

    def __init__(self, name, description="", is_active=True):
        self.name = name
        self.description = description
        self.is_active = is_active
        self.id = None

    def to_dict(self):
        """Преобразовать в словарь для API"""
        return {
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):
        """Создать из словаря от API"""
        company = cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            is_active=data.get("is_active", True)
        )
        company.id = data.get("id")
        return company
