from src.main_page.price_request.new_request.locators import *
from src.main_page.price_request.new_request.specification import *
from src.main_page.price_request.new_request.basic_data import BasicData


class NewRequest(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.basic_data = Button(driver, BASIC_DATA_TAB, 'Основные данные', BasicData)
        self.specification = Button(driver, SPECIFICATION_TAB, 'Спецификация')

    def __enter__(self):
        self._data = BasicData(self._driver)
        return self._data

    def __exit__(self, exc_type, exc_val, exc_tb):
        spec_type = None
        match self._data.life_cycle.get_value():
            case "НР":
                spec_type = NrSpecification
            case "СР":
                spec_type = ServiceSpecification
            case "С":
                spec_type = SeriesSpecification

        self.specification = Button(self._driver, SPECIFICATION_TAB, 'Спецификация', spec_type)
        return self
