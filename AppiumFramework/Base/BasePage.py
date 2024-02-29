from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFramework.utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self,driver):
        self.driver = driver

    def waitForElement(self,locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

        if locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, locatorValue))
            return element
        elif locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        else:
            self.log.info("Locator value" + locatorValue + "not found")

        return element

    def getElement(self, locatorValue, locatorType='xpath'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue " + locatorValue)
        except:
            self.log.info("Element not found with LocatorType: " + locatorType + " and with the locatorValue " + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType='xpath'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("Clicked on element with LocatorType: " + locatorType + " and with the locatorValue " + locatorValue)
        except:
            self.log.info(
                "Unable to click on element with LocatorType: " + locatorType + " and with the locatorValue " + locatorValue)

        return element

    def switchElement(self, locatorValue, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue " + locatorValue)
        except:
            self.log.info("Element not found with LocatorType: " + locatorType + " and with the locatorValue " + locatorValue)

        return element

    def screenShots(self, screenShotsName):
        fileName = screenShotsName + "_" +(time.strftime("%d_%m_%y_%H_%M_%S"))+".png"
        screenshotDirectory = "../Screenshots/"
        screenshotPath = screenshotDirectory + fileName

        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path: "+ screenshotPath)
        except:
            self.log.info("Unable to save screenshot to path: "+ screenshotPath)

