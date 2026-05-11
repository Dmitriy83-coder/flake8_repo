from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    # Локаторы для страницы профиля и списка "Буду смотреть"
    PROFILE_MENU = (By.CSS_SELECTOR, ".user-menu, .profile-dropdown, .user-pic")
    WATCHLIST_LINK = (By.CSS_SELECTOR, "a[href*='willwatch'], a[href*='future'], a:contains('Буду смотреть')")
    WATCHLIST_ITEMS = (By.CSS_SELECTOR, ".watch-list-item, .item, .film-item")
    WATCHLIST_FILM_TITLE = (By.CSS_SELECTOR, ".title, .name, .film-title")
    EMPTY_WATCHLIST = (By.CSS_SELECTOR, ".empty, .nothing-found, .no-items")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход в список 'Буду смотреть'")
    def go_to_watchlist(self) -> None:
        """Перейти на страницу со списком 'Буду смотреть'"""
        # Открываем меню профиля
        self.click(self.PROFILE_MENU)
        self.handle_captcha_if_present()

        # Переходим в раздел "Буду смотреть"
        self.click(self.WATCHLIST_LINK)
        self.handle_captcha_if_present()

    @allure.step("Получение списка фильмов из 'Буду смотреть'")
    def get_watchlist_films(self) -> list:
        """Получить список названий фильмов из 'Буду смотреть'"""
        try:
            items = self.find_elements(self.WATCHLIST_ITEMS)
            film_titles = []
            for item in items:
                try:
                    title_element = item.find_element(*self.WATCHLIST_FILM_TITLE)
                    film_titles.append(title_element.text)
                except:
                    continue
            return film_titles
        except:
            return []

    @allure.step("Проверка наличия фильма в списке 'Буду смотреть'")
    def is_film_in_watchlist(self, film_name: str) -> bool:
        """Проверить, находится ли фильм в списке 'Буду смотреть'"""
        films = self.get_watchlist_films()
        return any(film_name.lower() in film.lower() for film in films)

    @allure.step("Очистка списка 'Буду смотреть' (перед тестом)")
    def clear_watchlist(self) -> None:
        """Удалить все фильмы из списка 'Буду смотреть' (для чистоты тестов)"""
        self.go_to_watchlist()

        # Находим все кнопки удаления
        remove_buttons = (By.CSS_SELECTOR, ".remove, .delete, .close, [title*='удалить']")

        try:
            buttons = self.find_elements(remove_buttons)
            for button in buttons:
                try:
                    button.click()
                    self.handle_captcha_if_present()
                    import time
                    time.sleep(1)
                except:
                    continue
        except:
            pass
