from playwright.sync_api import Page
from Playwright.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_SELECTOR: str = '#user-name'
    PASSWORD_SELECTOR: str = "#password"
    LOGIN_BUTTON_SELECTOR: str = "#login-button"

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_text_present_on_page("Products")
