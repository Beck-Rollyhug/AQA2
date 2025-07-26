from playwright.sync_api import sync_playwright

BASE_URL = 'https://www.saucedemo.com/'


def start_front_test():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(BASE_URL)

    browser.close()
    playwright.stop()
