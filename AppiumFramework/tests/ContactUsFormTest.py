import CustomLogger
from AppiumFramework.Base.DriverClass import Driver
import AppiumFramework.utilities.CustomLogger as cl
from AppiumFramework.Base.BasePage import BasePage
import time

driver1 = Driver()
log = cl.customLogger()
driver = driver1.getDriverMethod()
bp = BasePage(driver)
log.info("Launch App")

bp.screenShots("App-test")
bp.clickElement("//*[@text='Network & internet']", "xpath")
time.sleep(2)
bp.switchElement("com.android.settings:id/switchWidget","id")
bp.screenShots("TEST-OK")
