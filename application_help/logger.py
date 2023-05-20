import logging

"""
    Log Level:
    Critical > Error > Warning > Info > Debug
"""


class Logger(object):
    """
        None
    """
    logging.basicConfig(level=logging.DEBUG)  # LogLevel에 상관없이 모두 출력
    logging.FileHandler("logtest.log")

    @staticmethod
    def critical(msg: str):
        """
            None
        """
        logging.critical(msg)

    @staticmethod
    def error(msg: str):
        """
            None
        """
        logging.error(msg)

    @staticmethod
    def warning(msg: str):
        """
            None
        """
        logging.warning(msg)

    @staticmethod
    def info(msg: str):
        """
            None
        """
        logging.info(msg)

    @staticmethod
    def debug(msg: str):
        """
            None
        """
        logging.debug(msg)


Logger.critical("critical")
Logger.error("error")
Logger.warning("warning")
Logger.info("info")
Logger.debug("debug")
