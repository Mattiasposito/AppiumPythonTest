import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel3XL',
    appPackage='com.android.settings',
    appActivity='.Settings',
)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

driver.find_element(AppiumBy.XPATH, "//*[@text='Network & internet']").click()
time.sleep(2)
driver.find_element(AppiumBy.ID, "com.android.settings:id/switchWidget").click()
time.sleep(2)
driver.find_element(AppiumBy.ID, "com.android.settings:id/switchWidget").click()


input()