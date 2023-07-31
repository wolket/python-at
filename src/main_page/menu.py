from src.base_page import BasePage
from src.components.button import Button
from src.main_page.locators import *
from src.main_page.price_request import PriceRequest


class Menu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.rkm = Button(driver, PK, 'PK', MenuPK)


class MenuPK(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_request = Button(driver, PRICE, 'Запрос', PriceRequest)
