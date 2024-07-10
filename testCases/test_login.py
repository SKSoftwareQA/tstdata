from playwright.sync_api._generated import Browser, Page
import pytest
from playwright.sync_api import sync_playwright
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


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


class Test_Login_001:
    config = ReadConfig()  # Create an instance of ReadConfig
    baseURL = config.getApplicationURL()
    username = config.getApplicationUsername()
    password = config.getApplicaitonpassword()

    logger = LogGen.loggen()

    def test_homepage_title(self, page: Page):
        self.logger.info("**************** Test Login 001 **********")
        self.logger.info("**************** Verifying the Homepage Title **********")
        page.goto(self.baseURL)
        pagetitle = page.title()
        if pagetitle == "Your store. Login":
            self.logger.info("**************** Homepage Title TC is Passed **********")
            assert True
        else:
            self.logger.error("**************** Homepage Title TC is Failed **********")
            assert False

    def test_login(self, page: Page):
        self.logger.info("****************Verifying the Login Functionality**********")
        page.goto(self.baseURL)
        lp = LoginPage(page)  # Create an instance of LoginPage
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        #lp.setPassword(self.password)  # Correct method name setPassword
        lp.clickLogin()
        page.wait_for_timeout(3000)
        pagetitle01 = page.url
        print(pagetitle01)
        if pagetitle01 == "https://admin-demo.nopcommerce.com/admin/":
            page.screenshot(path="./Screenshots/loginpassed.png")
            assert True
            self.logger.info("****************Login TC passed**********")
        else:
            page.screenshot(path="./Screenshots/loginfailed.png")
            self.logger.error("****************Login TC Failed**********")
            assert False
