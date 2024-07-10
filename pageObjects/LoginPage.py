
import pytest


class LoginPage:
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    button_login_type = "button[type='submit']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver= driver

    
    def setUserName(self, username):
        self.driver.wait_for_selector(self.textbox_username_id).fill('')
        self.driver.wait_for_selector(self.textbox_username_id).type(username)

    def setpassword(self, password):
        self.driver.wait_for_selector(self.textbox_password_id).fill('')
        self.driver.wait_for_selector(self.textbox_password_id).type(password)

    def clickLogin(self):
        self.driver.wait_for_selector(self.button_login_type).click()
    
    def clickLogout(self):
        self.driver.wait_for_selector(self.link_logout_xpath).click()

    




