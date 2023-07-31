from selenium.webdriver.support.wait import WebDriverWait

from src.base_page import BasePage
from src.components.button import Button
from src.components.combo_box import ComboBoxFind
from src.main_page.site_selection.locators import *
from selenium.webdriver.support import expected_conditions as ec


class SiteSelection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.confirm = Button(driver, CONFIRM, 'Подтвердить')
        self.selection = ComboBoxFind(driver, FIELD, 'Площадка')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        value = self.selection.get_value()
        self.confirm.click()
        self._wait_destroy(FIELD)
        from src.main_page.locators import CHOOSE_PLATFORM
        WebDriverWait(self._driver, 5).until(ec.text_to_be_present_in_element(CHOOSE_PLATFORM, value))
