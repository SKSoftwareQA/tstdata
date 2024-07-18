from playwright.sync_api._generated import Browser, Page
import pytest
from playwright.sync_api import sync_playwright
# from pageObjects.LoginPage import LoginPage
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()



@pytest.fixture(scope="function")
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()


    def test_login(self, page: Page):
        userurl= "https://demo.nopcommerce.com/"
        page.goto(self.userurl)
        username = page.wait_for_selector("//input[@id='Email']").fill("deepakmittal@amwebtech.com")
        password = page.wait_for_selector("//input[@id='Password']").fill("test@1234")
        loginbutton = page.wait_for_selector("//button[normalize-space()='Log in']").click()




