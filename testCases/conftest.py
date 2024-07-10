# from playwright.sync_api import sync_playwright
# import pytest

# # Fixture to set up the browser
# @pytest.fixture(scope="session")
# def setup(request):
#     # Get the browser type from the command line option
#     browser_type = request.config.getoption("--browser")
#     playwright = sync_playwright().start()

#     # Select the browser type
#     if browser_type == "chromium":
#         browser = playwright.chromium.launch(headless=False)
#         print("Testing on the Chrome Browser (Chromium)")
#     elif browser_type == "firefox":
#         browser = playwright.firefox.launch(headless=False)
#         print("Testing on the Firefox Browser")
#     elif browser_type == "webkit":
#         browser = playwright.webkit.launch(headless=False)
#         print("Testing on the WebKit Browser")
#     else:
#         raise ValueError(f"Unsupported browser: {browser_type}")

#     # Provide browser to the tests
#     yield browser

#     # Close the browser after the test
#     browser.close()
#     playwright.stop()

# # Fixture to parse command-line option
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chromium", help="Type of browser. E.g. chromium, firefox, webkit.")

# @pytest.fixture(scope="session")
# def browser_type(request):
#     return request.config.getoption("--browser")
