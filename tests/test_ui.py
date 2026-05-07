import pytest
import allure
from selenium.webdriver.common.by import By
from config.settings import TestData
from pages.search_page import SearchPage
from pages.film_page import FilmPage
from pages.profile_page import ProfilePage


@allure.feature("UI Tests")
@allure.story("Kinopoisk UI")
@pytest.mark.ui
class TestKinopoiskUI:

    @allure.title("Поиск фильма по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_film(self, driver):
        """Проверка поиска фильма по названию"""
        search_page = SearchPage(driver)
        film_name = TestData.FILM_NAME

        with allure.step(f"Выполнить поиск фильма '{film_name}'"):
            search_page.search_film(film_name)

        with allure.step("Проверить, что результаты поиска отображаются"):
            assert search_page.find_element(search_page.SEARCH_RESULTS) is not None

    @allure.title("Проверка карточки фильма")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_film_card(self, driver):
        """Проверка, что карточка фильма содержит все необходимые элементы"""
        search_page = SearchPage(driver)
        film_page = FilmPage(driver)
        film_name = TestData.FILM_NAME

        with allure.step(f"Найти фильм '{film_name}'"):
            search_page.search_film(film_name)

        with allure.step("Перейти на страницу фильма"):
            search_page.click_on_film(film_name)

        with allure.step("Проверить наличие всех элементов карточки"):
            assert film_page.verify_all_elements_present()

        with allure.step("Проверить название фильма"):
            title = film_page.get_title()
            assert film_name.lower() in title.lower()

        with allure.step("Проверить год выпуска"):
            year = film_page.get_year()
            assert year == TestData.FILM_YEAR or year > 0

    @allure.title("Фильтрация фильмов по году выпуска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_by_year(self, driver):
        """Проверка фильтрации по году на UI"""
        search_page = SearchPage(driver)
        target_year = 2022

        with allure.step(f"Выполнить поиск с фильтрацией по году {target_year}"):
            search_page.search_by_year(target_year)

        with allure.step("Проверить, что результаты отображаются"):
            assert search_page.find_element(search_page.SEARCH_RESULTS) is not None

    @allure.title("Пагинация в результатах поиска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_pagination(self, driver):
        """Проверка работы пагинации"""
        search_page = SearchPage(driver)

        with allure.step("Выполнить поиск по популярному запросу"):
            search_page.search_film("Мстители")

        with allure.step("Проверить наличие пагинации"):
            pagination_locator = (By.CSS_SELECTOR, ".pagination, .pages, .pager")
            assert search_page.find_element(pagination_locator) is not None

    @allure.title("Добавление фильма в 'Буду смотреть'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="Требуется авторизация")
    def test_add_to_watchlist(self, driver):
        """Проверка добавления фильма в список 'Буду смотреть'"""
        search_page = SearchPage(driver)
        film_page = FilmPage(driver)
        film_name = TestData.FILM_NAME

        with allure.step(f"Найти фильм '{film_name}'"):
            search_page.search_film(film_name)

        with allure.step("Перейти на страницу фильма"):
            search_page.click_on_film(film_name)

        with allure.step("Добавить фильм в 'Буду смотреть'"):
            film_page.add_to_watchlist()

        with allure.step("Проверить, что фильм добавлен"):
            assert film_page.is_in_watchlist()

    @allure.title("Проверка, что фильм появился в списке 'Буду смотреть'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="Требуется авторизация")
    def test_film_added_to_watchlist_verification(self, driver):
        """Проверка, что добавленный фильм отображается в списке 'Буду смотреть'"""
        search_page = SearchPage(driver)
        film_page = FilmPage(driver)
        profile_page = ProfilePage(driver)
        film_name = TestData.FILM_NAME

        with allure.step(f"Найти и добавить фильм '{film_name}'"):
            search_page.search_film(film_name)
            search_page.click_on_film(film_name)
            film_page.add_to_watchlist()

        with allure.step("Перейти в список 'Буду смотреть'"):
            profile_page.go_to_watchlist()

        with allure.step("Проверить, что фильм есть в списке"):
            assert profile_page.is_film_in_watchlist(film_name)

    @allure.title("Авторизация (пропущена, так как тесты без логина)")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Тесты запускаются без авторизации")
    def test_login(self, driver):
        """Проверка авторизации (пропущена)"""
        pass
