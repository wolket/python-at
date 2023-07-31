from selenium.webdriver.common.by import By

from src.base_page import BasePage


class ToolBar(BasePage):
    def __init__(self, driver, grid):
        super().__init__(driver)

        self._tool_bar = grid.find_element(By.XPATH, ".//*[contains(@class, 'dx-datagrid-header-panel')]")
