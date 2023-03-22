from appium.webdriver.common.appiumby import AppiumBy

from assignments.base.test_config import AppiumConfig


class TestHyundai(AppiumConfig):
    def test_sign_up(self):
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/txt_signup").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtFullname").send_keys('John')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtMobileNumber").send_keys(
            '9988776655')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtEmailAddress").send_keys(
            'abc@xyz.com')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtPasswordRegis").send_keys('Abc@1234')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtConfirmedPasswordRegis").send_keys('Abc@1234')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/checkAcceptTermsCondition").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/btnRegisterOnRegis").click()
