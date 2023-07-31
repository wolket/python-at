import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.base_page import BasePage


class Cell(BasePage):
    def __init__(self, driver, table, _row_, _column_, open_el=None):
        super().__init__(driver)

        self._table = table
        self._column = _column_
        self._row = _row_

        self._open_el = open_el

    def _get_cell(self, _row_, _column_):
        return self._table.find_element(By.XPATH, f".//tr[@aria-rowindex='{_row_}']/td[@aria-colindex='{_column_}']")

    def get_row(self):
        from src.components.grid.table.row import Row
        return Row(self._driver, self._table, self._row)

    def click(self):
        with allure.step(f"Клик на ячейку (строка: {self._row}, колонка: {self._column})"):
            ActionChains(self._driver).click(self._get_cell(self._row, self._column)).perform()
        return self

    def double_click(self):
        with allure.step(f"Двойной клик на ячейку (строка: {self._row}, колонка: {self._column})"):
            ActionChains(self._driver).double_click(self._get_cell(self._row, self._column)).perform()

        if self._open_el:
            return self._open_el(self._driver)
        else:
            return self
