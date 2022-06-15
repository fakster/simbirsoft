from selenium.webdriver.common.by import By


class GoogleSearchLocators:
    SEARCH_STRING = (By.CSS_SELECTOR,'input.gLFyf')
    BUTTON_SEARCH = (By.CSS_SELECTOR,'input.gNO89b')

class CalculatorPageLocators:
    ONE = (By.CSS_SELECTOR, '[jsname="N10B9"]')
    TWO = (By.CSS_SELECTOR, '[jsname="lVjWed"]')
    THREE = (By.CSS_SELECTOR, '[jsname="KN1kY"]')
    MULTIPLY = (By.CSS_SELECTOR, '[jsname="YovRWb"]')
    MINUS = (By.CSS_SELECTOR, '[jsname="pPHzQc"]')
    PLUS = (By.CSS_SELECTOR, '[jsname="XSr6wc"]')
    EQUAL = (By.CSS_SELECTOR, '[jsname="Pt8tGc"]')
    MEMORY_STRING = (By.CSS_SELECTOR,'[jsname="ubtiRe"]')
    RESULT = (By.CSS_SELECTOR,'[jsname="VssY5c"]')
