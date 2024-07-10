from playwright.sync_api._generated import Browser, Page
import pytest
from playwright.sync_api import sync_playwright, expect
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


class Test_add_new_customer_003:
    config = ReadConfig()  # Create an instance of ReadConfig
    baseURL = config.getApplicationURL()
    username = config.getApplicationUsername()
    password = config.getApplicaitonpassword()

    logger = LogGen.loggen()

 

    def test_login(self, page: Page):
        self.logger.info("****************Verifying the add mew customer Functionality**********")
        page.goto(self.baseURL)
        lp = LoginPage(page)  # Create an instance of LoginPage
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        #lp.setPassword(self.password)  # Correct method name setPassword
        lp.clickLogin()
        page.wait_for_timeout(3000)
        page.wait_for_selector("(//a[@class='nav-link active'])[1]").click()
        page.wait_for_timeout(3000)
        page.wait_for_selector("(//a[@class='nav-link'])[21]").click()
        page.wait_for_selector("//a[@href='/Admin/Customer/List']").click()
        
        search_cust = page.wait_for_selector("//input[@id='SearchEmail']").fill("vanik00@gmail.com")

        page.wait_for_selector("//button[@id='search-customers']").click()
        
        search_result = page.get_by_text("No data available in table").highlight()
        if search_result==True:
            assert True
        else:
            assert False

        # if search_result==True:
        #     assert True
        #     print("No Customer Found")
        # else:
        #     assert False
        #     print("Costomer found")