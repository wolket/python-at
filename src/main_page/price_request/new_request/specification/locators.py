from selenium.webdriver.common.by import By

NOMENCLATURE_OBJECT_FIELD = (By.NAME, "outer_nomenclature_name")
QUANTITY_BUY_FIELD = (By.XPATH, ".//input[contains(@id, '_quantity')]")

ADD_STAGE = (By.XPATH, ".//span[text() = 'Этапы']/ancestor-or-self::div[contains(@class, 'dx-field-item-has-group')]//i[@class = 'dx-icon dx-icon-edit-button-addrow']/ancestor-or-self::div[contains(@class, 'dx-button-content')]")
ADD_SERVICE = (By.XPATH, ".//span[text() = 'Объекты калькуляции']/ancestor-or-self::div[contains(@class, 'dx-field-item-has-group')]//i[@class = 'dx-icon dx-icon-edit-button-addrow']/ancestor-or-self::div[contains(@class, 'dx-button-content')]")
ADD_DELIVERY = (By.XPATH, "//*[text()='Объекты калькуляции']/..//*[@aria-label='Панель инструментов таблицы данных']//*[@role='button' and @title='Добавить' and @aria-label='add']")

STAGE_NUMBER = (By.XPATH, ".//table//td[@aria-colindex = 1]//input[@class = 'dx-texteditor-input']")
STAGE_NAME = (By.XPATH, ".//table//td[@aria-colindex = 2]//input[@class = 'dx-texteditor-input']")
STAGE_PRICE = (By.XPATH, ".//table//td[@aria-colindex = 3]//input[@class = 'dx-texteditor-input']")
STAGE_DATE_START = (By.XPATH, ".//table//td[@aria-colindex = 4]//input[@class = 'dx-texteditor-input']")
STAGE_DATE_END = (By.XPATH, ".//table//td[@aria-colindex = 5]//input[@class = 'dx-texteditor-input']")

SERVICE_NAME = (By.XPATH, ".//table//td[@aria-colindex = 1]//input[@class = 'dx-texteditor-input']")
SERVICE_OBJECT = (By.XPATH, ".//table//td[@aria-colindex = 2]//input[@class = 'dx-texteditor-input']")
SERVICE_PLACE = (By.XPATH, ".//table//td[@aria-colindex = 3]//input[@class = 'dx-texteditor-input']")
SERVICE_RECIPIENT = (By.XPATH, ".//table//td[@aria-colindex = 4]//input[@class = 'dx-texteditor-input']")
SERVICE_QUANTITY = (By.XPATH, ".//table//td[@aria-colindex = 7]//input[@class = 'dx-texteditor-input']")
SERVICE_DATE_START = (By.XPATH, ".//table//td[@aria-colindex = 8]//input[@class = 'dx-texteditor-input']")
SERVICE_DATE_END = (By.XPATH, ".//table//td[@aria-colindex = 9]//input[@class = 'dx-texteditor-input']")

DELIVERY_NAME = (By.NAME, 'title')
DELIVERY_MEASUREMENT = (By.NAME, 'unit_of_measurement')
DELIVERY_QUANTITY = (By.XPATH, "//*[@name='quantity']/..//input[@role='spinbutton']")
DELIVERY_DATE = (By.XPATH, "//*[@name='delivery_date']/..//input[@role='combobox']")

SAVE_OBJECT = (By.XPATH, ".//td/a[@title = 'Сохранить']")
SAVE_DELIVERY = (By.XPATH, "//*[text()='Поставка']/ancestor-or-self::*[contains(@class, 'dx-overlay-content')]//*[@role='button' and @title='Сохранить' and @aria-label='save']")
