import allure
from selenium.webdriver.common.by import By

from src.base_page import BasePage


class ComboBox(BasePage):
    def __init__(self, driver, locator, name):
        super().__init__(driver)
        self._locator = locator
        self._name = name

    def choose(self, value):
        with allure.step(f"Выбор значения '{value}' в поле '{self._name}'"):
            self._find_element(self._locator).click()
            self._find_element(self._LIST_ITEM(value)).click()
        return self

    def get_value(self):
        return self._find_element(self._locator).get_attribute('value')

    @staticmethod
    def _LIST_ITEM(value):
        return By.XPATH, f"//*[contains(@class, 'dx-dropdownlist-popup-wrapper')]//*[text()='{value}']"


class ComboBoxFind(ComboBox):
    def choose(self, value):
        with allure.step(f"Выбор значения '{value}' в поле '{self._name}'"):
            el = self._find_element(self._locator)
            el.click()
            el.clear()
            el.send_keys(value)
            self._find_element(self._LIST_ITEM(value)).click()
        return self
