from src.base_page import BasePage
from src.components.button import Button
from src.components.input import Input
from src.components.combo_box import ComboBox
from src.main_page.price_request.new_request.basic_data.executor_item import ExecutorItem
from src.main_page.price_request.new_request.basic_data.locators import *


class BasicData(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add = Button(driver, ADD_MAIN_EXECUTOR_BTN, 'Добавить', ExecutorItem)
        self.request_number = Input(driver, REQUEST_NUMBER_FIELD, 'Номер запроса')
        self.life_cycle = ComboBox(driver, LIFE_CYCLE_FIELD, 'Жизненный цикл')
        self.supplier = ComboBox(driver, METHOD_CHOICE_SUPPLIER_FIELD, 'Способ определения поставщика')
        self.save = Button(driver, SAVE_BASIC_DATA_BTN, 'Сохранить')
