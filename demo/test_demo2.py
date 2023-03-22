from appium.webdriver.common.appiumby import AppiumBy

from demo.test_config import AppiumConfig


class TestAppium(AppiumConfig):
    def test_app_lunch(self):
        get_dismiss_button = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
        if len(get_dismiss_button) > 0:
            get_dismiss_button[0].click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[contains(@content-desc,'username')]").send_keys(
            'abc@xyz.com')
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys(
            'abc@xyz')

        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)
