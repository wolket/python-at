from src.base_page import BasePage
from src.components.button import Button
from src.components.combo_box import ComboBoxFind
from src.main_page.price_request.new_request.basic_data.locators import *


class ExecutorItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.name = ComboBoxFind(driver, NAME_FIELD, "Наименование")
        self.save = Button(driver, SAVE_EXECUTOR, "Сохранить исполнителя")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save.click()
