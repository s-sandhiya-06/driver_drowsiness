import logging

logging.basicConfig(filename="driver.log", level=logging.INFO)

class Logger:
    @staticmethod
    def log(event):
        logging.info(event)
