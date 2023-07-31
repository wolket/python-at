import allure
from src.main_page.price_request import PriceRequest


@allure.story('Создание')
@allure.title('Создание запроса с фиксированной ценой')
@allure.testcase('TEST-1', 'TEST-1')
def test_create_request_fix_price(main_page):
    main_page.header.change_platform('Test platform')

    send_request = open_rkm(main_page)
    send_request.search.fill("Python_test_")._wait_load()
    send_request.grid.table.get_cell("Получено", "Статус запроса").click()
    send_request.manipulations.click()
    go_to_rkm_versions = send_request.go_pk_versions.click()
    create_rkm_version = go_to_rkm_versions.add.click()
    create_rkm_version.unit_calc.choose('Единица работы')
    create_rkm_version.save.click()


@allure.story('Создание')
@allure.title('Создание запроса с ориентировочной ценой')
@allure.testcase('TEST-2', 'TEST-2')
def test_create_request_estim_price(main_page):
    main_page.header.change_platform('Test platform')

    send_request = open_rkm(main_page)
    send_request.search.fill("Python_test_")._wait_load()
    send_request.grid.table.get_cell("Получено", "Статус запроса").click()
    send_request.manipulations.click()
    go_to_rkm_versions = send_request.go_pk_versions.click()
    create_rkm_version = go_to_rkm_versions.add.click()
    create_rkm_version.check_box.click()
    create_rkm_version.unit_calc.choose('Единица работы')
    create_rkm_version.save.click()


def open_rkm(main_page) -> PriceRequest:
    return main_page.menu.rkm.click() \
        .price_request.click()
