from src.base_page import BasePage
from src.components.button import Button
from src.components.input import Input
from src.main_page.price_request.new_request.specification.locators import *


class Stage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.save = Button(driver, SAVE_OBJECT, 'Сохранение этапа')
        self.number = Input(driver, STAGE_NUMBER, 'Номер этапа')
        self.name = Input(driver, STAGE_NAME, 'Наименование этапа')
        self.price = Input(driver, STAGE_PRICE, 'Стоимость')
        self.date_start = Input(driver, STAGE_DATE_START, 'Дата начала этапа')
        self.date_end = Input(driver, STAGE_DATE_END, 'Дата завершения этапа')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save.click()


class Service(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.save = Button(driver, SAVE_OBJECT, 'Сохранение сервиса')
        self.name = Input(driver, SERVICE_NAME, 'Наименование')
        self.object = Input(driver, SERVICE_OBJECT, 'Объект')
        self.place = Input(driver, SERVICE_PLACE, 'Место поставки')
        self.recipient = Input(driver, SERVICE_RECIPIENT, 'Получатель')
        self.quantity = Input(driver, SERVICE_QUANTITY, 'Количество')
        self.date_start = Input(driver, SERVICE_DATE_START, 'Дата начала')
        self.date_end = Input(driver, SERVICE_DATE_END, 'Дата окончания')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save.click()


class Delivery(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.save = Button(driver, SAVE_DELIVERY, 'Сохранение поставки')
        self.name = Input(driver, DELIVERY_NAME, 'Наименование')
        self.measurement = Input(driver, DELIVERY_MEASUREMENT, 'Единицы измерения')
        self.quantity = Input(driver, DELIVERY_QUANTITY, 'Количество')
        self.date = Input(driver, DELIVERY_DATE, 'Дата поставки')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save.click()
