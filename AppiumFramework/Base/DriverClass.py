from appium import webdriver
from appium.options.android import UiAutomator2Options


class Driver:

    def getDriverMethod(selfself):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Pixel3XL',
            appPackage='com.android.settings',
            appActivity='.Settings',
        )
        appium_server_url = 'http://localhost:4723'
        driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

        return driver