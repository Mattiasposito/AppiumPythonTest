import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='VirtualDevicePixel',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)
#appium test
appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    """def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()"""

    def test_find_battery(self) -> None:
        el = self.driver.find_element(AppiumBy.XPATH, '//*[@text="Network & internet"]')
        el.click()


