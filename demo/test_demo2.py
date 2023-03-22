from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

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

    def test_invalid_sign_up_email_test(self):
        get_dismiss_button = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
        if len(get_dismiss_button) > 0:
            get_dismiss_button[0].click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Settings']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'email')]").click()

        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='First name']").send_keys("john")
        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Last name']").send_keys("peter")

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").click()

        # choose Aug
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").clear()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").send_keys(
            "Oct")

        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH,
                                 "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys("23")

        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH,
                                 "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys("1997")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Email address']").send_keys("test123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys("welcome123")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='CREATE']").click()

        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        assert_that(actual_error).is_equal_to('There was an issue signing in')
