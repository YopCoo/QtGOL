from util.Log import Log
from PyQt5.QtWidgets import *
from PyQt5.Qt import QPalette
from ui.configSelector import Ui_Dialog as config_dialog
from service.ServiceUserContext import ServiceUserContext

logger = Log().getLogger(__name__)


class ConfigWindow(QDialog, config_dialog):

    def __init__(self):
        super(ConfigWindow, self).__init__()
        logger.info("Begin Initialisation ConfigWindow")
        self.setupUi(self)
        # Services
        self.colorPicker = QColorDialog()
        self.serviceUc = ServiceUserContext()
        # Object
        self.config = self.serviceUc.getLastUserContext()
        self.isDefaut = False
        # Widget
        self.colorizedButton()
        self.sb_xcell.setValue(self.config.x_cell)
        self.sb_ycell.setValue(self.config.y_cell)
        self.sb_sizecell.setValue(self.config.size_cell)
        # Actions
        self.btn_newcolor.clicked.connect(self.setNewColor)
        self.btn_activecolor.clicked.connect(self.setActiveColor)
        self.btn_inactivecolor.clicked.connect(self.setInactiveColor)
        self.btn_accept.clicked.connect(self.notifyConfig)
        self.btn_cancel.clicked.connect(self.closeConfig)
        self.btn_defaut.clicked.connect(self.defautConfig)
        # Observer
        self.observers = []
        logger.info("End Initialisation ConfigWindow")
        # Display Condition
        if self.serviceUc.getUserContext("LAST_CONFIG") is None:
            self.btn_defaut.setDisabled(True)


    def defautConfig(self):
        self.config = self.serviceUc.getUserContext("DEFAUT")
        self.serviceUc.deleteUserContext("LAST_CONFIG")
        self.isDefaut = True
        self.notifyConfig()

    def addObserver(self,observer):
        logger.info("ConfigWindow addObserver : " + observer.__str__())
        self.observers.append(observer)

    def delObserver(self,observer):
        logger.info("ConfigWindow delObserver : " + observer.__str__())
        self.observers.remove(observer)

    def notifyConfig(self):
        logger.info("sendConfig")
        if not self.isDefaut:
            self.config.size_cell = self.sb_sizecell.value()
            self.config.x_cell = self.sb_xcell.value()
            self.config.y_cell = self.sb_ycell.value()
            self.serviceUc.saveOrUpdateUserContext(self.config, "LAST_CONFIG")
        for observer in self.observers:
            logger.debug("Observer send config : " + self.config.__str__())
            observer.onConfigChanged(self.config)
        self.isDefaut = False
        self.closeConfig()

    def closeConfig(self):
        self.close()

    def setNewColor(self):
        logger.debug("setNewColor : " + self.config.new_color.name().__str__())
        self.colorPicker.setCurrentColor(self.config.new_color)
        self.config.new_color = self.colorPicker.getColor(self.config.new_color)
        logger.debug((" to " + self.config.new_color.name().__str__()))
        self.colorizedButton()

    def setActiveColor(self):
        logger.debug("setActiveColor : " + self.config.active_color.name().__str__())
        self.colorPicker.setCurrentColor(self.config.active_color)
        self.config.active_color = self.colorPicker.getColor(self.config.active_color)
        logger.debug((" to " + self.config.active_color.name().__str__()))
        self.colorizedButton()

    def setInactiveColor(self):
        logger.debug("setInactiveColor : " + self.config.inactive_color.name().__str__())
        self.colorPicker.setCurrentColor(self.config.inactive_color)
        self.config.inactive_color = self.colorPicker.getColor(self.config.inactive_color)
        logger.debug((" to " + self.config.inactive_color.name().__str__()))
        self.colorizedButton()

    def colorizedButton(self):
        self.btn_newcolor.setPalette(QPalette(self.config.new_color))
        self.btn_activecolor.setPalette(QPalette(self.config.active_color))
        self.btn_inactivecolor.setPalette(QPalette(self.config.inactive_color))
