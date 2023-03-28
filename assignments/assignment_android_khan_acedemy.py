import os
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    driver = None
    app = None

    @pytest.fixture(scope='function', autouse=True)
    def config(self):
        self.app = os.getcwd() + '\\test_data\\khan-academy-7-3-2.apk'
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(20)

        yield
        time.sleep(5)
        self.driver.quit()


class TestInstallKhan(AppiumConfig):
    def test_uninstall_app(self):
        if self.driver.is_app_installed("org.khanacademy.android"):
            self.driver.remove_app("org.khanacademy.android")

    def test_install_app(self):
        self.driver.install_app(self.app)
        self.driver.activate_app("org.khanacademy.android")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Allow']").click()

    def test_course_challenge(self):
        self.driver.activate_app("org.khanacademy.android")

        get_dismiss_button = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
        if len(get_dismiss_button) > 0:
            get_dismiss_button[0].click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search tab").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Math']").click()

        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Trigonometry")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Trigonometry')]").click()

# 6. Scroll and click on Class 12 Math (India) - Not found that
#
# 7. Scroll and click on Take Course Chanllenge
#
# 8. Scroll and click on Option C
#
# 9. Get the message shown and print it