import pytest
from appium import webdriver


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            "bstack:options": {
                "userName": "gosaihardik1",
                "accessKey": "ZwsiyCq9XUqmzxzmp4xW",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1-ios",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
        pass
# 3.	Enter username as john
# 4.	Enter password as john123
# 5.	Get the error message shown and assert it
