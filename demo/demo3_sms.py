import time

import pytest
from appium import webdriver

"""Automation using ANDROID_UIAUTOMATOR"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):
    def test_list_sms(self):
        time.sleep(5)
        messages = self.driver.execute_script("mobile: listSms", {"max": 1})
        print(messages)
        print(messages["items"])
        print(messages["total"])
        print(messages["items"][0])
        print(messages["items"][0]["body"])
