from selenium.webdriver.common.by import *


ADD_BTN = (By.XPATH, ".//div[@title = 'Добавить']")
SEARCH_FIELD = (By.XPATH, "//div[@class = 'dx-item dx-toolbar-item dx-toolbar-button']//input[@class = 'dx-texteditor-input']")
GRID = (By.ID, "requestsGrid")
MANIPULATIONS_BTN = (By.XPATH, "//span[text() = 'Операции']")
SEND_REQUEST_BTN = (By.XPATH, ".//div[(@title = 'Отправить запрос')]")
GO_PK_VERSIONS_BTN = (By.XPATH, ".//div[text() = 'Перейти к версиям']")
