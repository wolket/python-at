import allure

from src.base_page import BasePage


class Input(BasePage):
    def __init__(self, driver, locator, name):
        super().__init__(driver)
        self._locator = locator
        self._name = name

    def fill(self, value):
        with allure.step(f"Заполнение '{self._name}' значением '{value}'"):
            self._find_element(self._locator).send_keys(value)
        return self
