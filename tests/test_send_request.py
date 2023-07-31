import allure
from src.main_page.price_request import PriceRequest


@allure.story('Отправка')
@allure.title('Отправка Запроса цены НР')
@allure.testcase('TEST-6', 'TEST-6')
def test_send_nir(main_page):
    main_page.header.change_platform("Test platform")

    send_request = open_rkm(main_page)
    send_request.search.fill("Python_test_НР_")._wait_load()
    send_request.grid.table.get_cell("Черновик", "Статус запроса").click()
    send_request.manipulations.click()
    request_to_main = send_request.send.click()
    request_to_main.grid.table.get_cell(1, 1).click()
    request_to_main.send_to_main.click()


@allure.story('Отправка')
@allure.title('Отправка Запроса цены СР')
@allure.testcase('TEST-7', 'TEST-7')
def test_send_service(main_page):
    main_page.header.change_platform("Test platform")

    send_request = open_rkm(main_page)
    send_request.search.fill("Python_test_СР")._wait_load()
    send_request.grid.table.get_cell("Черновик", "Статус запроса").click()
    send_request.manipulations.click()
    request_to_main = send_request.send.click()
    request_to_main.grid.table.get_cell(1, 1).click()
    request_to_main.send_to_main.click()


@allure.story('Отправка')
@allure.title('Отправка Запроса цены С')
@allure.testcase('TEST-8', 'TEST-8')
def test_send_series(main_page):
    main_page.header.change_platform("Test platform")

    send_request = open_rkm(main_page)
    send_request.search.fill("Python_test_С")._wait_load()
    send_request.grid.table.get_cell("Черновик", "Статус запроса").click()
    send_request.manipulations.click()
    request_to_main = send_request.send.click()
    request_to_main.grid.table.get_cell(1, 1).click()
    request_to_main.send_to_main.click()


# Открытие ЭФ и нового запроса
def open_rkm(main_page) -> PriceRequest:
    return main_page.menu.rkm.click()\
        .price_request.click()
