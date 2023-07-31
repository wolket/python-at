from selenium.webdriver.common.by import By

from src.base_page import BasePage

from src.components.grid.table.row import Row
from src.components.grid.table.cell import Cell


class Table(BasePage):
    def __init__(self, driver, grid, header, open_el=None):
        super().__init__(driver)

        self._open_el = open_el

        self._table = grid.find_element(By.XPATH, ".//*[contains(@class, 'dx-datagrid-rowsview')]//*[contains(@class, 'dx-datagrid-content')]")
        self._header = header

    def get_cell(self, _row_, _column_):
        if type(_column_) is str:
            _column_ = self._header.get_col_index(_column_)

        if type(_row_) is str:
            _row_ = int(self._table.find_element(By.XPATH, f".//td[text()='{_row_}' and @aria-colindex='{_column_}']/ancestor-or-self::tr").get_attribute("aria-rowindex"))

        return Cell(self._driver, self._table, _row_, _column_, self._open_el)

    def get_row(self, _row_):
        return Row(self._driver, self._table, int(_row_), self._open_el)
