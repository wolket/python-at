from src.base_page import BasePage
from src.main_page.header import Header
from src.main_page.menu import Menu


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.menu = Menu(driver)
