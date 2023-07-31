import allure

from src.base_page import BasePage


class Button(BasePage):
    def __init__(self, driver, locator, name, open_el=None):
        super().__init__(driver)
        self._locator = locator
        self._name = name
        self._open_el = open_el

    def click(self):
        with allure.step(f"Клик на кнопку: '{self._name}'"):
            self._find_element(self._locator).click()

        if self._open_el:
            return self._open_el(self._driver)
        else:
            return self
