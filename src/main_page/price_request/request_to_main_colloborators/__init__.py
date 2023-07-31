from src.base_page import BasePage
from src.components.button import Button
from src.components.grid import Grid
from src.main_page.price_request.request_to_main_colloborators.locators import *


class SendMainColoborators(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from src.main_page.price_request import PriceRequest
        self.send_to_main = Button(driver, SEND_BTN, 'Отправить', PriceRequest)
        self.grid = Grid(driver, GRID, SendMainColoborators)
