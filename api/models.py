from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class Film:
    """Модель фильма"""
    id: int
    name: Optional[str] = None
    alternative_name: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None
    rating: Optional[dict] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Film":
        """Создать объект Film из словаря"""
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            alternative_name=data.get("alternative_name"),
            year=data.get("year"),
            description=data.get("description"),
            rating=data.get("rating")
        )


@dataclass
class FilmsResponse:
    """Модель ответа со списком фильмов"""
    docs: List[Film]
    total: int
    limit: int
    page: int
    pages: int

    @classmethod
    def from_dict(cls, data: dict) -> "FilmsResponse":
        """Создать объект FilmsResponse из словаря"""
        docs = [Film.from_dict(film) for film in data.get("docs", [])]
        return cls(
            docs=docs,
            total=data.get("total", 0),
            limit=data.get("limit", 0),
            page=data.get("page", 0),
            pages=data.get("pages", 0)
        )


@dataclass
class ErrorResponse:
    """Модель ответа с ошибкой"""
    message: str
    status_code: int

    @classmethod
    def from_dict(cls, data: dict, status_code: int) -> "ErrorResponse":
        """Создать объект ErrorResponse из словаря"""
        return cls(
            message=data.get("message", data.get("error", "Unknown error")),
            status_code=status_code
        )
