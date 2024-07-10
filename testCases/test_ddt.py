from playwright.sync_api._generated import Browser, Page
import pytest
from playwright.sync_api import sync_playwright
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities


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


class Test_DDT_Login_002:
    config = ReadConfig()  # Create an instance of ReadConfig
    baseURL = config.getApplicationURL()
    path = "./TestData/testdata.xlsx"
    

    logger = LogGen.loggen()


    def test_login_ddt(self, page: Page):
        #self.logger.info("****************Test 002 DDT Login Functionality**********")
        #self.logger.info("****************Verifying the DDT Login Functionality**********")
        page.goto(self.baseURL)
        lp = LoginPage(page)  # Create an instance of LoginPage

        self.rows= XLUtilities.getRowCount(self.path, 'Sheet1')
        print("Number of rows",self.rows)
        
        lst_status=[]

        for r in range(2,self.rows):
            self.user = XLUtilities.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtilities.readData(self.path, 'Sheet1',r,2)
            self.exp = XLUtilities.readData(self.path, 'Sheet1',r,3)
            lp.setUserName(self.user)
            lp.setpassword(self.password)
            lp.clickLogin()
            page.wait_for_timeout(3000)
            act_title= page.url
            ext_title = "https://admin-demo.nopcommerce.com/admin/"

            if ext_title == act_title:
                if self.exp == "Pass":
                    self.logger.info("****************The DDT Login TC is passed**********")
                    lst_status.append("Pass")
                    assert True
                    lp.clickLogout()
                else:
                    self.logger.info("****************The DDT Login TC is Failed**********")
                    assert False
            
        
        self.logger.info("****************DDT Login TC passed**********")
        