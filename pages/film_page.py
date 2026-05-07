from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import UIConfig
import allure


class FilmPage(BasePage):
    # Локаторы
    FILM_TITLE = (By.CSS_SELECTOR, "h1, .movie-title, .title")
    FILM_YEAR = (By.CSS_SELECTOR, ".info, .year, .movie-info")
    FILM_RATING = (By.CSS_SELECTOR, ".rating, .rating-value, .kp-rating")
    FILM_DESCRIPTION = (By.CSS_SELECTOR, ".description, .synopsis")
    WATCH_BUTTON = (By.CSS_SELECTOR, ".watch-link, .add-to-watch, button[title*='смотреть']")
    WILL_WATCH_BUTTON = (By.CSS_SELECTOR, ".will-watch, .add-to-future, button[title*='Буду смотреть']")
    WILL_WATCH_STATUS = (By.CSS_SELECTOR, ".in-watchlist, .added-to-watch, .status-added")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получение названия фильма")
    def get_title(self) -> str:
        """Получить название фильма"""
        return self.get_text(self.FILM_TITLE)

    @allure.step("Получение года выпуска фильма")
    def get_year(self) -> int:
        """Получить год выпуска фильма из текста"""
        year_text = self.get_text(self.FILM_YEAR)
        # Извлекаем год из текста (например "2014, США" -> 2014)
        import re
        years = re.findall(r'\b(19|20)\d{2}\b', year_text)
        if years:
            return int(years[0])
        return 0

    @allure.step("Получение рейтинга фильма")
    def get_rating(self) -> float:
        """Получить рейтинг фильма"""
        rating_text = self.get_text(self.FILM_RATING)
        try:
            return float(rating_text.replace(',', '.'))
        except:
            return 0.0

    @allure.step("Добавление в 'Буду смотреть'")
    def add_to_watchlist(self) -> None:
        """Добавить фильм в список 'Буду смотреть'"""
        self.click(self.WILL_WATCH_BUTTON)
        self.handle_captcha_if_present()

    @allure.step("Проверка, что фильм добавлен в 'Буду смотреть'")
    def is_in_watchlist(self) -> bool:
        """Проверить, находится ли фильм в списке 'Буду смотреть'"""
        try:
            return self.find_element(self.WILL_WATCH_STATUS) is not None
        except:
            return False

    @allure.step("Проверка наличия всех элементов карточки фильма")
    def verify_all_elements_present(self) -> bool:
        """Проверить наличие всех основных элементов"""
        try:
            self.find_element(self.FILM_TITLE)
            self.find_element(self.FILM_YEAR)
            self.find_element(self.FILM_RATING)
            return True
        except:
            return False
