from selenium.webdriver.common.by import By

REQUEST_NUMBER_FIELD = (By.NAME, "code")
LIFE_CYCLE_FIELD = (By.XPATH, ".//div[@data-dx_placeholder = 'Выберите жизненный цикл запроса']//preceding-sibling::input[@class = 'dx-texteditor-input']")
METHOD_CHOICE_SUPPLIER_FIELD = (By.XPATH, ".//input[contains(@id, 'contractor_determination_id')]")

ADD_MAIN_EXECUTOR_BTN = (By.XPATH, ".//div[@title = 'Добавить строку']")
SAVE_BASIC_DATA_BTN = (By.XPATH, ".//div[@title = 'Сохранить']")

NAME_FIELD = (By.XPATH, ".//table//div[@data-dx_placeholder = 'Выбрать...']//preceding-sibling::input[@class = 'dx-texteditor-input']")
SAVE_EXECUTOR = (By.XPATH, ".//td/a[@title = 'Сохранить']")
