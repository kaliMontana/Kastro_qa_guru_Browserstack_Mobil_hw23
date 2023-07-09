import pytest
from appium import webdriver
from selene.support.shared import browser

import config
from browserstack_mobil.utils.attach import add_screenshot, attach_video


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = config.settings.timeout

    yield
    attach_video(browser)
    add_screenshot(browser)

    browser.quit()
