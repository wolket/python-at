from selenium.webdriver.common.by import By

from src.base_page import BasePage


class Header(BasePage):
    def __init__(self, driver, grid):
        super().__init__(driver)

        self._grid = grid

    def get_col_index(self, value):
        return int(self._grid.find_element(By.XPATH, f".//*[contains(@class, 'dx-datagrid-headers')]//table//*[text()='{value}']/ancestor-or-self::td").get_attribute("aria-colindex"))
