from src.base_page import BasePage
from src.components.button import Button
from src.components.grid import Grid
from src.components.input import Input
from src.main_page.price_request.locators import *
from src.main_page.price_request.new_request import NewRequest


class PriceRequest(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._wait_load()
        from src.main_page.price_request.pk_versions import PKVersions
        self.add = Button(driver, ADD_BTN, "Добавить", NewRequest)
        self.grid = Grid(driver, GRID, NewRequest)
        self.search = Input(driver, SEARCH_FIELD, "Поиск")
        self.manipulations = Button(driver, MANIPULATIONS_BTN, "Операции")
        from src.main_page.price_request.request_to_main_colloborators import SendMainColoborators
        self.send = Button(driver, SEND_REQUEST_BTN, "Отправить запрос исполнителю", SendMainColoborators)
        self.go_pk_versions = Button(driver, GO_PK_VERSIONS_BTN, "Перейти к версиям РКМ", PKVersions)
