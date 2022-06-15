from .locators import CalculatorPageLocators,GoogleSearchLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_element(self,locator,timeout=10):
        return WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located(locator),
                                                         message="Can't find locator{}".format(locator))

    def go_to_calculator_page(self):
        search_string = self.find_element(GoogleSearchLocators.SEARCH_STRING)
        search_string.send_keys("Калькулятор")
        button = self.find_element(GoogleSearchLocators.BUTTON_SEARCH)
        button.click()

    def write_digits_to_calculator(self):
        one = self.find_element(CalculatorPageLocators.ONE)
        multiply = self.find_element(CalculatorPageLocators.MULTIPLY)
        two = self.find_element(CalculatorPageLocators.TWO)
        minus = self.find_element(CalculatorPageLocators.MINUS)
        three = self.find_element(CalculatorPageLocators.THREE)
        plus = self.find_element(CalculatorPageLocators.PLUS)
        equal = self.find_element(CalculatorPageLocators.EQUAL)
        one.click()
        multiply.click()
        two.click()
        minus.click()
        three.click()
        plus.click()
        one.click()
        equal.click()

    def check_memory_string(self):
        assert self.find_element(CalculatorPageLocators.MEMORY_STRING).text == '1 × 2 - 3 + 1 =', \
            'Formula from task is not in memory string'

    def check_result(self):
        assert self.find_element(CalculatorPageLocators.RESULT).text == '0', \
            'Expected result is not present'
