import allure
import pytest
import json
import base64

from selenium.common import WebDriverException
from selenium.webdriver import *
from selenium.webdriver.common.proxy import ProxyType
from os.path import *
from src.main_page import MainPage


def pytest_addoption(parser):
    """ Параметр для передачи пути до файла конфигурации """

    parser.addoption(
        "--config",
        action="store",
        default="./settings/settings.json",
        help="Environment to run tests against (e.g. 'staging' or 'production')"
    )


@pytest.fixture(scope="function")
def driver(request):
    """ Фикстура создания сессии """

    # Load setting file
    with open(join(dirname(abspath(__file__)), request.config.getoption('--config'))) as config:
        settings = json.load(config)

    # Prepare firefox options
    options = FirefoxOptions()
    options.set_capability(name="selenoid:options", value={"enableVNC": True,
                                                           "timeZone": "Europe/Moscow"})
    options.proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': settings["proxy_host"] + ':' + settings["proxy_port"]
    })

    # Start session
    driver = Remote(command_executor=settings["selenium_host"],
                    options=options)

    # Open project
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get("http://" + settings["domain"] + "/?qaauth=" + auth_format(settings["username"], settings["password"]))

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    """ Фикстура, которая сразу возвращает объект страницы """

    yield MainPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """ После каждого теста прикладывает скриншот если тест провалился """

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            # attach screenshot on test failure
            with allure.step("Дополнительная информация"):
                add_allure_information(driver)


def add_allure_information(driver):
    """ Функция приложения скриншота """

    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            driver.page_source,
            name="HTML",
            attachment_type=allure.attachment_type.HTML
        )
    except WebDriverException:
        pass


def auth_format(username, password):
    """ Возвращает формат авторизации """

    auth = base64.b64encode(str(username + ':' + password).encode('utf-8')).decode('utf-8')
    return auth
