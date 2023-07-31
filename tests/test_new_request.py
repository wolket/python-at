import random
import time
from datetime import datetime, timedelta

import allure

from src.main_page.price_request import PriceRequest


@allure.story('Создание')
@allure.title('Создание Запроса цены НР')
@allure.testcase('TEST-3', 'TEST-3')
def test_create_nir(main_page):
    main_page.header.change_platform("Test platform")

    new_request = open_rkm(main_page).add.click()

    specification_tab = fill_data(new_request, "НР")
    specification_tab.nomenclature.fill(f"Python_test_{str(random.randint(0, 1000))}")
    specification_tab.quantity.fill(str(random.randint(0, 1000)))

    with specification_tab.add.click() as stage:
        stage.number.fill("1")
        stage.name.fill("Наименование первого этапа")
        stage.date_start.fill("10.03.2023")
        stage.date_end.fill("12.04.2023")

    with specification_tab.add.click() as stage:
        stage.number.fill("2")
        stage.name.fill("Наименование второго этапа")
        stage.date_start.fill("13.04.2023")
        stage.date_end.fill("12.01.2024")

    new_request.basic_data.click()\
        .save.click()


@allure.story('Создание')
@allure.title('Создание Запроса цены СР')
@allure.testcase('TEST-4', 'TEST-4')
def test_create_service(main_page):
    main_page.header.change_platform("Test platform")

    new_request = open_rkm(main_page).add.click()

    specification_tab = fill_data(new_request, "СР")
    specification_tab.subject.fill(f"Python_test_{str(random.randint(0, 1000))}")

    with specification_tab.add.click() as service:
        service.name.fill("С")
        service.object.fill("Авто-тест")
        service.place.fill("Москва")
        service.recipient.fill("Jenkins")
        service.quantity.fill(str(random.randint(0, 1000)))
        service.date_start.fill((datetime.today()).strftime('%d.%m.%Y'))
        service.date_end.fill((datetime.today() + timedelta(days=random.randint(0, 1000))).strftime('%d.%m.%Y'))

    new_request.basic_data.click() \
        .save.click()


@allure.story('Создание')
@allure.title('Создание Запроса цены С')
@allure.testcase('TEST-5', 'TEST-5')
def test_create_series(main_page):
    main_page.header.change_platform("Test platform")

    new_request = open_rkm(main_page).add.click()

    specification_tab = fill_data(new_request, "С")
    specification_tab.subject.fill(f"Python_test_{str(random.randint(0, 1000))}")

    with specification_tab.add.click() as delivery:
        delivery.name.fill("Тест")
        delivery.measurement.fill("шт.")
        delivery.date.fill((datetime.today()).strftime('%d.%m.%Y'))
        delivery.quantity.fill(str(random.randint(0, 1000)))

    new_request.basic_data.click() \
        .save.click()


# Заполнение основной информации
def fill_data(new_request, life_cycle):
    with new_request as data:
        data.request_number.fill(f"Python_test_{life_cycle}_{(datetime.today()).strftime('%d.%m.%Y.%H.%M.%S')}")
        data.life_cycle.choose(life_cycle)
        data.supplier.choose("Закупки")

        with data.add.click() as executor:
            executor.name.choose('Test platform')

    return new_request.specification.click()


# Открытие ЭФ Создание нового запроса
def open_rkm(main_page) -> PriceRequest:
    return main_page.menu.rkm.click() \
        .price_request.click()


def test_open_request(main_page):
    main_page.header.change_platform("Test platform")

    price_request = open_rkm(main_page)

    price_request.grid.table.get_cell(3, 1).click().double_click().specification.click()
