import logging
import logging.config


class Log:

    logging.config.fileConfig("qtgol/util/log.ini")

    @staticmethod
    def getLogger(arg):
        return logging.getLogger(arg)
