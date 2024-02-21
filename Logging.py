import logging


logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',filename="test.log", datefmt='%d/%m/%y %I:%M:%S %p', level=logging.DEBUG)
logging.critical("This is critical")
logging.error("This is a error message")
logging.warning("This is a warning message")
logging.info("This is a info message")
logging.debug("This is a debug message")