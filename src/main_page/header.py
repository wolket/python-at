from src.base_page import BasePage
from src.components.button import Button
from src.main_page.locators import *
from src.main_page.site_selection import SiteSelection


# Прописаны общие шаги для всех экранных форм
class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.choose_platform = Button(driver, CHOOSE_PLATFORM, 'Выбор площадки', SiteSelection)

    def change_platform(self, value):
        with self.choose_platform.click() as site_selection:
            site_selection.selection.choose(value)

        return self
