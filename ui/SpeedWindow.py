from util.Log import Log
from PyQt5.QtWidgets import *
from ui.speedSelector import Ui_Dialog as speed_dialog
from service.ServiceUserContext import ServiceUserContext

logger = Log().getLogger(__name__)


class SpeedWindow(QDialog, speed_dialog):

    def __init__(self):
        super(SpeedWindow, self).__init__()
        logger.info("Degin Initialisation SpeedWindow")
        self.setupUi(self)
        # Service
        self.serviceUc = ServiceUserContext()
        # Object
        self.speed = self.serviceUc.getLastUserContext().speed
        self.delta = 50
        self.btn_lower.clicked.connect(self.lowerSpeed)
        self.btn_upper.clicked.connect(self.upperSpeed)
        # Indicator
        genParSec = round(1 / (self.speed / 1000), 2)
        self.ind_speed.setText(str(genParSec) + " gen / sec.")
        # Observer
        self.observers = []
        logger.info("End Initialisation SpeedWindow")

    def addObserver(self, observer):
        logger.info("SpeedWindow addObserver : " + observer.__str__())
        self.observers.append(observer)

    def delObserver(self, observer):
        logger.info("SpeedWindow delObserver : " + observer.__str__())
        self.observers.remove(observer)

    def changeSpeed(self, val):
        self.speed = self.speed + val
        if self.speed <= 50:
            self.speed = 50
        if self.speed >= 1000:
                self.speed = 1000
        genParSec = round(1 / (self.speed/1000), 2)
        self.ind_speed.setText(str(genParSec) + " gen / sec.")
        self.notifySpeed(self.speed)

    def lowerSpeed(self):
        self.changeSpeed(self.delta)

    def upperSpeed(self):
        self.changeSpeed(-self.delta)

    def notifySpeed(self,speed):
        logger.info("SpeedWindow sendSpeed")
        for observer in self.observers:
            logger.debug("Observer send speed : " + str(speed))
            observer.onSpeedChange(speed)
