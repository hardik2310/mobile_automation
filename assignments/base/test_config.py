import os
import time

import pytest
from appium import webdriver


class AppiumConfig:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def config(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": os.getcwd() + '\\test_data\\hyundai_app.apk',
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(20)

        yield
        time.sleep(5)
        self.driver.quit()
