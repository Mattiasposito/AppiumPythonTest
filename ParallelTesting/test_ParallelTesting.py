import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


def deviceDriver(deviceId, sysPort):
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Pixel3XL',
        udid= deviceId,
        systemPort = sysPort,
        appPackage='com.android.settings',
        appActivity='.Settings',
    )

    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    return driver

def enterText(driver):
    driver.find_element(AppiumBy.XPATH, "//*[@text='Network & internet']").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "com.android.settings:id/switchWidget").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "com.android.settings:id/switchWidget").click()
    time.sleep(2)
    driver.quit()


def test_deviceTest():
    d1 = deviceDriver('V24A00208', 8200)
    d2 = deviceDriver('emulator-5554', 8201)

    enterText(d1)
    enterText(d2)