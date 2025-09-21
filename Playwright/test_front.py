import pytest
from playwright.sync_api import sync_playwright

from Playwright.pages.checkout_page import CheckoutPage
from Playwright.pages.inventory_page import InventoryPage
from Playwright.pages.login_page import LoginPage

BASE_URL = 'https://www.saucedemo.com/'


# def start_front_test():
#     playwright = sync_playwright().start()

#     browser = playwright.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()
#     page.goto(BASE_URL)

#     browser.close()
#     playwright.stop()


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('jhon', 'snow', '12345')
