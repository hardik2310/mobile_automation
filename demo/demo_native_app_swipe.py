import time
from os import getcwd

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Automation using ANDROID_UIAUTOMATOR"""


class AppiumConfig:
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


class TestArts(AppiumConfig):
    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        time.sleep(5)

        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Art of Asia")'}
        self.driver.execute_script("mobile: scroll", para_dic)

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art of Asia']").click()

        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().textContains("Himala")'}
        self.driver.execute_script("mobile: scroll", para_dic)

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("Himala")').click()
