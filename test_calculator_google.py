from .pages.base_page import BasePage


def test_can_go_to_calculator_page(browser):
    link = "https://www.google.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_calculator_page()
    page.write_digits_to_calculator()
    page.check_memory_string()
    page.check_result()
