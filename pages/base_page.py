from selenium.webdriver.common.by import By
from .locators import CalculatorPageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_calculator_page(self):
        input = self.browser.find_element(By.CSS_SELECTOR, 'input.gLFyf')
        input.send_keys("Калькулятор")
        button = self.browser.find_element(By.CSS_SELECTOR, 'input.gNO89b')
        button.click()

    def write_digits_to_calculator(self):
        one = self.browser.find_element(*CalculatorPageLocators.ONE)
        multiply = self.browser.find_element(*CalculatorPageLocators.MULTIPLY)
        two = self.browser.find_element(*CalculatorPageLocators.TWO)
        minus = self.browser.find_element(*CalculatorPageLocators.MINUS)
        three = self.browser.find_element(*CalculatorPageLocators.THREE)
        plus = self.browser.find_element(*CalculatorPageLocators.PLUS)
        equal = self.browser.find_element(*CalculatorPageLocators.EQUAL)
        one.click()
        multiply.click()
        two.click()
        minus.click()
        three.click()
        plus.click()
        one.click()
        equal.click()

    def check_memory_string(self):
        assert self.browser.find_element(*CalculatorPageLocators.MEMORY_STRING).text == '1 × 2 - 3 + 1 =', \
            'Formula from task is not in memory string'

    def check_result(self):
        assert self.browser.find_element(*CalculatorPageLocators.RESULT).text == '0', \
            'Expected result is not present'
