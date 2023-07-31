from selenium.webdriver.common.by import By

UNIT_FIELD = (By.XPATH, ".//input[contains(@id, 'costing_unit_id')]")
END_EXECUTION_DATE_FIELD = (By.XPATH, "//input[contains(@id, 'end_execution_date')]")
SAVE_BTN = (By.XPATH, ".//div[@title = 'Сохранить']")
RADIO_BTN = (By.XPATH, "//div[contains(@class, 'dx-radiobutton') and contains(@aria-checked, 'false')]")
