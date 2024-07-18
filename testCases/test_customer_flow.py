# from playwright.sync_api._generated import Browser, Page
# import pytest
# from playwright.sync_api import sync_playwright


# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()


# @pytest.fixture(scope="function")
# def page(browser: Browser):
#     page = browser.new_page()
#     yield page
#     page.close()


# def test_logincustomer(page):
#         userurl= "https://demo.nopcommerce.com/login?returnurl=%2F"
#         page.goto("https://demo.nopcommerce.com/login?returnurl=%2F")
#         page.wait_for_selector("//input[@id='Email']").fill("deepakmittal@amwebtech.com")
#         page.wait_for_selector("//input[@id='Password']").fill("test@1234")
#         page.wait_for_selector("//button[normalize-space()='Log in']").click()
       
#         electornics= page.wait_for_selector("//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']").hover()
#         select_cell_phones_dropdown = page.wait_for_selector("//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']").click()
#         page.wait_for_timeout(3000)
#         add_to_cart= page.wait_for_selector("//div[@class='item-grid']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
#         page.wait_for_timeout(3000)
#         go_to_cart= page.wait_for_selector("//span[@class='cart-label']").click()
#         checkbox= page.wait_for_selector("//input[@id='termsofservice']").check()
#         click_checkout_button =  page.wait_for_selector("//button[@id='checkout']").click()
#         if page.get_by_text == "Select a billing address from your address book or enter a new address.":
#             page.wait_for_selector("//button[@id='delete-billing-address-button']").click()
#         else: 
#             page.wait_for_selector("//button[@name='save']").click()

#             select_country_India =  page.get_by_label('Country').select_option('India')
#             city = page.wait_for_selector("//input[@id='BillingNewAddress_City']").fill("Indore")
#             address = page.wait_for_selector("//input[@id='BillingNewAddress_Address1']").fill("Main Street Main Road")
#             zipcode= page.wait_for_selector("//input[@id='BillingNewAddress_ZipPostalCode']").fill("452001")
#             phone_number = page.wait_for_selector("//input[@id='BillingNewAddress_PhoneNumber']").fill("9425957878")
#             checkout_button = page.wait_for_selector("//button[@onclick='if (!window.__cfRLUnblockHandlers) return false; Billing.save()']").click()
#             page.wait_for_timeout(3000)
        
        
               
#             page.wait_for_selector("//button[@name='save']").click()

#             page.wait_for_timeout(3000)
#             page.locator("xpath=//button[@class='button-1 shipping-method-next-step-button'])[1]").click()
#             page.wait_for_timeout(3000)
#             page.wait_for_selector("(//button[@class='button-1 payment-method-next-step-button'])[1]").click()
#             page.wait_for_timeout(3000)
#             page.wait_for_selector("(//button[@class='button-1 payment-info-next-step-button'])[1]").click()
#             page.wait_for_selector("//button[normalize-space()='Confirm']").click()


#         # page.wait_for_selector("//button[normalize-space()='Confirm']").click()
#         page.wait_for_timeout(9000)