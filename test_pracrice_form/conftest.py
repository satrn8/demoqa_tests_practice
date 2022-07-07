from selene.support.shared import browser
import pytest


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    browser.config.base_url = "https://demoqa.com"
    browser.config.browser_name = "chrome"
    # browser.config.window_width = 500
    # browser.config.window_height = 800

