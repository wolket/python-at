import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.base_page import BasePage


class Row(BasePage):
    def __init__(self, driver, table, row, open_el=None):
        super().__init__(driver)

        self._table = table
        self._row = row

        self._open_el = open_el

    def _get_row(self, _row_):
        return self._table.find_element(By.XPATH, f".//tr[@aria-rowindex='{_row_}']")

    def get_cell(self, _column_):
        from src.components.grid.table.cell import Cell
        return Cell(self._driver, self._table, self._row, _column_)

    def click(self):
        with allure.step(f"Клик на строку (строка: {self._row})"):
            ActionChains(self._driver).click(self._get_row(self._row)).perform()
        return self

    def double_click(self):
        with allure.step(f"Двойной клик на строку (строка: {self._row})"):
            ActionChains(self._driver).double_click(self._get_row(self._row)).perform()

        if self._open_el:
            return self._open_el(self._driver)
        else:
            return self
