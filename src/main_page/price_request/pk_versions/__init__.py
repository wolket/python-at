from src.base_page import BasePage
from src.components.button import Button
from src.main_page.price_request.pk_versions.create_pk_version import CreatePKVersion
from src.main_page.price_request.pk_versions.locators import ADD_BTN


class PKVersions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add = Button(driver, ADD_BTN, "Добавить", CreatePKVersion)
