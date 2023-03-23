from os import getcwd

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Automation using ANDROID_UIAUTOMATOR"""


class AppiumConfig:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": getcwd() + '\khan-academy-7-3-2.apk'
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestLogin(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'UiSelector().descriptionContains("e-mail address")').send_keys("Abc")

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'UiSelector().descriptionContains("password")').send_keys(
            "Abc123")

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in").instance(1)').click()

        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'UiSelector().textContains("issue")').get_attribute("text")
        print(actual_error)
