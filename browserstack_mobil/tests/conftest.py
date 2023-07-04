import pytest
from appium import webdriver
from selene.support.shared import browser

import config


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = config.settings.timeout

    yield

    browser.quit()
