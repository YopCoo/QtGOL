import logging
import logging.config


class Log:

    def __init__(self):
        self._log = logging.config.fileConfig("util/log.ini")

    def getLogger(self,arg):
        return logging.getLogger(arg)
