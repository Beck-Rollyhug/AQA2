from playwright.sync_api import Page
from Playwright.pages.base_page import BasePage

WITH_DELAY: int = 100


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR: str = "[id='checkout']"
    FIRST_NAME_SELECTOR: str = '#first-name'
    LAST_NAME_SELECTOR: str = '#last-name'
    POSTAL_CODE_SELECTOR: str = 'input[name="postalCode"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = '/checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, firstname, lastname, postal_code):
        self.wait_for_selector_and_type(
            self.FIRST_NAME_SELECTOR, firstname, WITH_DELAY)
        self.wait_for_selector_and_type(
            self.LAST_NAME_SELECTOR, lastname, WITH_DELAY)
        self.wait_for_selector_and_type(
            self.POSTAL_CODE_SELECTOR, postal_code, WITH_DELAY)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
