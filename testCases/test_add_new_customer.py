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
        page.wait_for_selector("(//a[normalize-space()='Add new'])[1]").click()
        
        cust_email = page.wait_for_selector("//input[@id='Email']").fill("fulltest@test.com")
        cust_password= page.wait_for_selector("//input[@id='Password']").fill("password")
        cust_firstname = page.wait_for_selector("//input[@id='FirstName']").fill("test first name")
        cust_lastname = page.wait_for_selector("//input[@id='LastName']").fill("test second name")
        cust_gender = page.wait_for_selector("//input[@id='Gender_Male']").click()
        cust_dob = page.wait_for_selector("//input[@id='DateOfBirth']").fill("2011-11-11")

        #page.get_by_label("Birth date").fill("2020-02-02")
        # page.wait_for_timeout(5000)
        cust_gender = page.wait_for_selector("//input[@id='Gender_Female']").check()
        
        cust_roles = page.get_by_label('Customer roles').select_option(label='Registered')
        #page.get_by_label('Customer roles').select_option(label='Vendors')
        button_save = page.wait_for_selector("(//button[@name='save'])[1]").click()
        # page_title = page.title()

        # if page_title == "Add a new customer / nopCommerce administration":
        #     print("**********failed*************")
        #     assert True
            

        # else:
        #     print("**********pased*************") 
        #     assert False

        page.wait_for_timeout(5000)
        
