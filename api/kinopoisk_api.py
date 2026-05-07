import requests
from typing import List, Optional
from config.settings import APIConfig, TestData
from api.models import Film, FilmsResponse, ErrorResponse


class KinopoiskAPI:
    def __init__(self):
        self.base_url = APIConfig.BASE_URL
        self.headers = APIConfig.HEADERS

    def get_all_films(self, limit: int = 10) -> FilmsResponse:
        """Получение списка всех фильмов"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"limit": limit}
        )
        response.raise_for_status()
        return FilmsResponse.from_dict(response.json())

    def get_films_with_limit(self, limit: int) -> FilmsResponse:
        """Получение фильмов с указанным лимитом"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"limit": limit}
        )
        response.raise_for_status()
        return FilmsResponse.from_dict(response.json())

    def get_film_by_id(self, film_id: int) -> Film:
        """Получение фильма по ID"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie/{film_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return Film.from_dict(response.json())

    def get_nonexistent_film(self, film_id: int) -> requests.Response:
        """Попытка получить несуществующий фильм"""
        return requests.get(
            f"{self.base_url}/v1.4/movie/{film_id}",
            headers=self.headers
        )

    def filter_by_year(self, year: int, limit: int = 10) -> FilmsResponse:
        """Фильтрация фильмов по году выпуска"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"year": year, "limit": limit}
        )
        response.raise_for_status()
        return FilmsResponse.from_dict(response.json())

    def filter_by_year_no_raise(self, year: int, limit: int = 10) -> requests.Response:
        """Фильтрация по году без raise_for_status (для негативных тестов)"""
        return requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"year": year, "limit": limit}
        )

    def filter_by_rating_imdb(self, rating_range: str) -> FilmsResponse:
        """Фильтрация по рейтингу IMDb"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"rating.imdb": rating_range, "limit": 10}
        )
        response.raise_for_status()
        return FilmsResponse.from_dict(response.json())

    def filter_by_year_and_genre(self, year: int, genre: str) -> FilmsResponse:
        """Фильтрация по году и жанру"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"year": year, "genres.name": genre, "limit": 10}
        )
        response.raise_for_status()
        return FilmsResponse.from_dict(response.json())

    def get_random_series(self) -> Film:
        """Получение случайного сериала"""
        response = requests.get(
            f"{self.base_url}/v1.4/movie/random",
            headers=self.headers,
            params={"type": "tv-series", "status": "announced"}
        )
        response.raise_for_status()
        return Film.from_dict(response.json())

    def filter_by_rating_kp(self, rating: float) -> requests.Response:
        """Фильтрация по рейтингу КП (включая невалидные)"""
        return requests.get(
            f"{self.base_url}/v1.4/movie",
            headers=self.headers,
            params={"rating.kp": rating}
        )
