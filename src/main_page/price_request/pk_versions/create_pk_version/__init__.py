from src.base_page import BasePage
from src.components.button import Button
from src.components.combo_box import ComboBox
from src.components.input import Input
from src.main_page.price_request.pk_versions.create_pk_version.locators import UNIT_FIELD, SAVE_BTN, RADIO_BTN, END_EXECUTION_DATE_FIELD


class CreatePKVersion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from src.main_page.price_request.pk_versions import PKVersions
        self.unit_calc = ComboBox(driver, UNIT_FIELD, "Калькуляционная единица")
        self.end_date = Input(driver, END_EXECUTION_DATE_FIELD, "Дата окончания выполнения")
        self.check_box = Button(driver, RADIO_BTN, "Чекбокс", CreatePKVersion)
        self.save = Button(driver, SAVE_BTN, "Сохранить", PKVersions)
