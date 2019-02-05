from qtgol.util.Log import Log
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt, QPen, QTimer
from qtgol.ui.mainwindow import Ui_MainWindow
from qtgol.model.Board import Board
from qtgol.ui.GolGraphicScene import GolGraphicScene
from qtgol.service.ServicePattern import ServicePattern
from qtgol.service.ServiceUserContext import ServiceUserContext
from qtgol.ui.ConfigWindow import ConfigWindow
from qtgol.ui.SpeedWindow import SpeedWindow


logger = Log().getLogger(__name__)


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        logger.info("Begin initialisation MainWindow.")
        self.setupUi(self)
        # Services
        self.servicePattern = ServicePattern()
        self.serviceUserContext = ServiceUserContext()

        self.config = self.serviceUserContext.getLastUserContext()
        # Windows
        self.speedWindow = None
        self.configWindow = None

        self.start = False
        self.board = None
        self.rect_statut = None
        self.scene = None

        self.initBoard(True)

        self.actionQuit.triggered.connect(self.close)
        self.actionstart_pause.triggered.connect(self.toggle_start)
        self.actionrefresh.triggered.connect(self.autogen)
        self.actionSpeed.triggered.connect(self.openSpeedWindow)
        self.actionConfig.triggered.connect(self.openConfigWindow)

        self.timer = QTimer()
        self.timer.setInterval(self.config.speed)
        self.timer.timeout.connect(self.nextgen)
        self.timer.start()
        self.show()
        logger.info("End initialisation MainWindow.")

    def openSpeedWindow(self):
        self.speedWindow = SpeedWindow()
        self.speedWindow.addObserver(self)
        self.speedWindow.show()

    def openConfigWindow(self):
        self.configWindow = ConfigWindow()
        self.configWindow.addObserver(self)
        self.configWindow.show()

    def toggle_start(self):
        pen = QPen(Qt.red)
        pen.setWidth(10)
        if self.start:
            logger.info("toggle_start : set Stop")
            self.start = False
            self.rect_statut = self.scene.addRect(0,0,self.config.x_cell*self.config.size_cell,self.config.y_cell*self.config.size_cell,pen)
        else:
            logger.info("toggle_start : set Start")
            self.start = True
            self.scene.removeItem(self.rect_statut)

    def close(self):
        logger.debug("close : begin closing window")
        origin_state = self.start
        self.start = False
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Question?")
        msgBox.setText("Do you want to quit?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            logger.info("close : Close application")
            QApplication.quit()
        else:
            logger.debug("close : cancel closing window")
            self.start = origin_state

    def clean(self):
        logger.info("clean : reset scene")
        self.scene.clean()
        self.lcd_generation.display(0)

    def onSizeCellChange(self):
        logger.info("onSizeCellChange : cell size changing, redraw scene")
        self.config.size_cell = self.sb_sizecell.value()
        self.scene = GolGraphicScene(self.board, self.config)
        if self.rect_statut:
            self.rect_statut.setRect(0,0,self.config.x_cell*self.config.size_cell,self.config.y_cell*self.config.size_cell)
        self.configScene()

    def onSpeedChange(self, speed):
        self.config.speed = speed
        self.timer.setInterval(self.config.speed)
        logger.info("onSpeedChange : set refresh to :"+str(self.config.speed)+"ms")

    def onConfigChanged(self, config):
        reloadBoard = False
        if (config.x_cell != self.config.x_cell) | (config.y_cell != self.config.y_cell):
            reloadBoard = True
        self.config = config
        self.initBoard(reloadBoard)
        logger.info("onConfigChanged : " + self.config.__str__())

    def autogen(self):
        self.board.autogen()
        self.scene.refreshScene()
        logger.info("autogen : randow cell creation on board")

    def nextgen(self):
        if self.start:
            self.board.nextgen()
            self.scene.refreshScene()
            logger.debug("nextgen : calculate next generation et refresh the scene")

    def keyPressEvent(self, event):
        logger.debug("keyPressEvent : pressed on : "+str(event.key()))
        if event.key() == Qt.Key_P:
            self.toggle_start()
        if event.key() == Qt.Key_A:
            self.autogen()
        if event.key() == Qt.Key_B:
            self.scene.clean()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.close()

    def initBoard(self, createBoard):
        if createBoard:
            logger.info("initBoard : create board")
            self.board = Board(self.config.x_cell, self.config.y_cell, self.config.density)
        self.scene = GolGraphicScene(self.board, self.config)
        self.configScene()
        self.scene.refreshScene()
        logger.info("initBoard : draw scene")

    def configScene(self):
        self.scene.setBackgroundBrush(self.config.inactive_color)
        if self.start == False:
            pen = QPen(Qt.red)
            pen.setWidth(10)
            self.rect_statut = self.scene.addRect(0, 0, self.config.x_cell * self.config.size_cell,
                                                  self.config.y_cell * self.config.size_cell, pen)
        self.canvas.setScene(self.scene)
        self.canvas.setFixedWidth(self.config.x_cell * self.config.size_cell)
        self.canvas.setFixedHeight(self.config.y_cell * self.config.size_cell)
        logger.info("configScene : configuration to draw scene")

    def defineStaticPattern(self):
        patternId = self.cb_staticPattern.itemData(self.cb_staticPattern.currentIndex())
        pattern = self.servicePattern.getPatternById(patternId)
        self.scene.setPattern(pattern)
        logger.info("Select Static pattern with id = "+str(patternId))

    def definePeriodicPattern(self):
        patternId = self.cb_periodicPattern.itemData(self.cb_periodicPattern.currentIndex())
        pattern = self.servicePattern.getPatternById(patternId)
        self.scene.setPattern(pattern)
        logger.info("Select Periodic pattern with id = " + str(patternId))

    def defineMovingPattern(self):
        patternId = self.cb_movingPattern.itemData(self.cb_movingPattern.currentIndex())
        pattern = self.servicePattern.getPatternById(patternId)
        self.scene.setPattern(pattern)
        logger.info("Select Moving pattern with id = " + str(patternId))
