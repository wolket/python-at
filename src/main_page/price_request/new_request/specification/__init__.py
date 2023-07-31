from src.main_page.price_request.new_request.specification.locators import *
from src.main_page.price_request.new_request.specification.item import *


class NrSpecification(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add = Button(driver, ADD_STAGE, 'Добавить этап', Stage)
        self.nomenclature = Input(driver, NOMENCLATURE_OBJECT_FIELD, 'Номенклатура')
        self.quantity = Input(driver, QUANTITY_BUY_FIELD, 'Количество закупки')


class ServiceSpecification(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add = Button(driver, ADD_SERVICE, 'Добавить сервис', Service)
        self.subject = Input(driver, NOMENCLATURE_OBJECT_FIELD, 'Предмет закупки')


class SeriesSpecification(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add = Button(driver, ADD_DELIVERY, 'Добавить поставку', Delivery)
        self.subject = Input(driver, NOMENCLATURE_OBJECT_FIELD, 'Предмет закупки')
