from selenium.webdriver.common.by import By

from src.base_page import BasePage


class Pager(BasePage):
    def __init__(self, driver, grid):
        super().__init__(driver)

        self._page_size = grid.find_element(By.XPATH, ".//*[contains(@class, 'dx-datagrid-pager')]//*[@class='dx-page-sizes']")
        self._pages = grid.find_element(By.XPATH, ".//*[contains(@class, 'dx-datagrid-pager')]//*[@class='dx-pages']")
