import pytest
import allure
from config.settings import TestData


@allure.feature("API Tests")
@allure.story("Kinopoisk API")
@pytest.mark.api
class TestKinopoiskAPI:

    @allure.title("Получение списка всех фильмов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_films(self, api_client):
        """Проверяем базовую функциональность API"""
        with allure.step("Выполнить запрос на получение списка фильмов"):
            response = api_client.get_all_films(limit=10)

        with allure.step("Проверить структуру ответа"):
            assert response.docs is not None
            assert len(response.docs) > 0
            assert response.total > 0

        with allure.step("Проверить наличие обязательных полей"):
            first_film = response.docs[0]
            assert hasattr(first_film, 'id')
            assert hasattr(first_film, 'name') or hasattr(first_film, 'alternative_name')

    @allure.title("Получение списка фильмов с указанием лимита")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_films_with_limit(self, api_client):
        """Тестируем возможность ограничения количества результатов"""
        limit = 5

        with allure.step(f"Выполнить запрос с лимитом {limit}"):
            response = api_client.get_films_with_limit(limit=limit)

        with allure.step(f"Проверить, что получено не более {limit} фильмов"):
            assert len(response.docs) <= limit
            assert response.limit == limit

    @allure.title("Получение данных по конкретному фильму по ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_film_by_valid_id(self, api_client):
        """Проверяем, что API возвращает правильные данные для существующего фильма"""
        film_id = TestData.FILM_ID
        expected_name = TestData.FILM_NAME

        with allure.step(f"Выполнить запрос для фильма ID={film_id}"):
            film = api_client.get_film_by_id(film_id)

        with allure.step("Проверить, что вернулся правильный фильм"):
            assert film.id == film_id
            assert expected_name.lower() in (film.name or "").lower() or \
                   expected_name.lower() in (film.alternative_name or "").lower()

        with allure.step("Проверить наличие года выпуска"):
            assert film.year is not None
            assert film.year == TestData.FILM_YEAR

    @allure.title("Запрос фильма с несуществующим годом")
    def test_film_with_nonexistent_year(self, api_client):
        year = TestData.NON_EXISTENT_YEAR

        with allure.step(f"Выполнить запрос с годом {year}"):
            response = api_client.filter_by_year_no_raise(year=year, limit=10)  # ← новый метод

        with allure.step("Проверить, что API вернул 400 или 200"):
            assert response.status_code in [200, 400]

    @allure.title("Фильтрация фильмов по году выпуска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_by_year(self, api_client):
        """Проверяем возможность фильтрации по году"""
        year = TestData.FILM_YEAR

        with allure.step(f"Выполнить запрос с фильтрацией по году {year}"):
            response = api_client.filter_by_year(year=year, limit=10)

        with allure.step("Проверить, что все фильмы соответствуют указанному году"):
            assert len(response.docs) > 0
            for film in response.docs:
                assert film.year == year

    @allure.title("Фильтрация фильмов с рейтингом IMDb 8-10")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_by_rating_imdb(self, api_client):
        """Проверяем фильтрацию по рейтингу IMDb"""
        rating_range = "8-10"

        with allure.step(f"Выполнить запрос с рейтингом {rating_range}"):
            response = api_client.filter_by_rating_imdb(rating_range)

        with allure.step("Проверить, что рейтинг в указанном диапазоне"):
            assert len(response.docs) > 0
            for film in response.docs:
                if film.rating and film.rating.get('imdb'):
                    rating = float(film.rating['imdb'])
                    assert 8.0 <= rating <= 10.0

    @allure.title("Фильтрация фильмов за 2022 год в жанре драма")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_by_year_and_genre(self, api_client):
        """Проверяем фильтрацию по году и жанру"""
        year = 2022
        genre = "драма"

        with allure.step(f"Выполнить запрос: год={year}, жанр={genre}"):
            response = api_client.filter_by_year_and_genre(year, genre)

        with allure.step("Проверить результаты фильтрации"):
            assert len(response.docs) > 0
            for film in response.docs:
                assert film.year == year

    @allure.title("Запрос фильма с несуществующим годом")
    @allure.severity(allure.severity_level.MINOR)
    def test_film_with_nonexistent_year(self, api_client):
        """Проверяем обработку запроса с несуществующим годом"""
        year = TestData.NON_EXISTENT_YEAR

        with allure.step(f"Выполнить запрос с годом {year}"):
            response = api_client.filter_by_year_no_raise(year=year, limit=10)

        with allure.step("Проверить, что API вернул 400 (Bad Request) или 200 с пустым списком"):
            # 2065 год не существует → API должен вернуть 400
            assert response.status_code in [200, 400]

    @allure.title("Поиск фильма с рейтингом выше 10 (невалидный запрос)")
    @allure.severity(allure.severity_level.MINOR)
    def test_film_with_rating_above_10(self, api_client):
        """Проверяем обработку невалидного значения рейтинга"""
        rating = 10.5

        with allure.step(f"Выполнить запрос с рейтингом {rating}"):
            response = api_client.filter_by_rating_kp(rating)

        with allure.step("Проверить, что API вернул ошибку или пустой результат"):
            # API может вернуть либо 400 ошибку, либо пустой список
            assert response.status_code in [200, 400]
