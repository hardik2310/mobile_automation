# C:\Users\112315\AppData\Local\Android\Sdk\platform-tools\adb.exe  devices
import time
from os import getcwd

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": getcwd() + '\khan-academy-7-3-2.apk'
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(20)

get_dismiss_button = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
if len(get_dismiss_button) > 0:
    get_dismiss_button[0].click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'username')]").send_keys(
    'abc@xyz.com')
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys('abc@xyz')
driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
actual_error = driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
print(actual_error)
actual_error = driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
print(actual_error)

time.sleep(5)
driver.quit()
