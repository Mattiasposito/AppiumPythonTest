import logging
import CustomLogger as cl

class CustomLoggerDemo():
    log = cl.customLogger()

    def methodeOne(self):
        self.log.critical("This is critical")
        self.log.error("This is message")
        self.log.warning("This is warning")
        self.log.info("This is info")
        self.log.debug("This is Debug")

    def methodeTwo(self):
        m2 = cl.customLogger()
        m2.critical('Critical msg')
        m2.error("error msg")
        m2.warning("warning msg")
        m2.info("info msg")
        m2.debug("debug msg")

cld = CustomLoggerDemo()
cld.methodeOne()
cld.methodeTwo()