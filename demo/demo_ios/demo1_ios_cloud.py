import time

from appium import webdriver

des_cap = {
    # Set URL of the application under test
    "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
    # Specify device and os_version for testing
    "deviceName": "iPhone 11 Pro",
    "platformVersion": "13",
    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName": "gosaihardik1",
        "accessKey": "ZwsiyCq9XUqmzxzmp4xW",
        "projectName": "First Python project",
        "buildName": "browserstack-build-1-ios",
        "sessionName": "BStack first_test-ios"
    }
}

driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)
print(driver.page_source)
time.sleep(5)
driver.quit()
