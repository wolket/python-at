from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _find_element(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(
            ec.element_to_be_clickable(locator))

    def _wait_destroy(self, locator):
        try:
            return WebDriverWait(self._driver, 3).until(
                ec.invisibility_of_element_located(locator))
        except StaleElementReferenceException:
            return None

    def _wait_load(self):
        try:
            loads = self._find_element((By.XPATH, "//*[contains(@class, 'dx-loadpanel-wrapper')]"), 2)
        except (TimeoutException, StaleElementReferenceException):
            return

        WebDriverWait(self._driver, 5).until(ec.invisibility_of_element(loads))
