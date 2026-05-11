from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.settings import UIConfig
import allure


class SearchPage(BasePage):
    # Локаторы
    SEARCH_INPUT = (By.NAME, "kp_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search_results, .results, .film-list")
    FILM_LINKS = (By.CSS_SELECTOR, ".search_results a, .results a, .film-item a")
    YEAR_FILTER = (By.CSS_SELECTOR, "select[name='m_act[year]'], .filter-year")
    YEAR_OPTION = (By.XPATH, "//select[@name='m_act[year]']/option[@value='{year}']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Поиск фильма: {film_name}")
    def search_film(self, film_name: str) -> None:
        """Выполнить поиск фильма"""
        self.open(UIConfig.BASE_URL)
        self.handle_captcha_if_present()

        # Вводим название в поиск
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(film_name)
        search_input.send_keys(Keys.RETURN)

        self.handle_captcha_if_present()

    @allure.step("Поиск фильма с фильтрацией по году: {year}")
    def search_by_year(self, year: int) -> None:
        """Поиск с фильтрацией по году"""
        self.open(UIConfig.BASE_URL)
        self.handle_captcha_if_present()

        # Открываем расширенный поиск или фильтр
        try:
            year_filter = self.find_element(self.YEAR_FILTER)
            year_filter.click()
            year_option = (By.XPATH, f"//select[@name='m_act[year]']/option[@value='{year}']")
            self.click(year_option)
        except:
            # Альтернативный способ: добавляем год в поисковый запрос
            search_input = self.find_element(self.SEARCH_INPUT)
            search_input.send_keys(f" {year}")
            search_input.send_keys(Keys.RETURN)

        self.handle_captcha_if_present()

    @allure.step("Переход на страницу фильма: {film_name}")
    def click_on_film(self, film_name: str) -> None:
        """Кликнуть по фильму в результатах поиска"""
        film_links = self.find_elements(self.FILM_LINKS)
        for link in film_links:
            if film_name.lower() in link.text.lower():
                link.click()
                break
        self.handle_captcha_if_present()
