from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt, QPen, QTimer
from ui.mainwindow import Ui_MainWindow
from model.Board import Board
from ui.GolGraphicScene import GolGraphicScene
from service.ServicePattern import ServicePattern
from service.ServiceUserContext import ServiceUserContext
from util.Log import Log


logger = Log().getLogger(__name__)

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        logger.info("Debut initialisation de la fenêtre principale.")
        # Services
        self.servicePattern = ServicePattern()
        self.serviceUserContext = ServiceUserContext()
        self.config = self.serviceUserContext.getUserContext("DEFAUT")

        self.start = False
        self.board = None
        self.rect_statut = None

        self.setupUi(self)
        self.scene = None
        self.scenePreview = None

        self.initBoard()
        self.initPreview()

        self.bt_quit.clicked.connect(self.close)
        self.bt_start.clicked.connect(self.toggle_start)
        self.bt_reset.clicked.connect(self.onConfigChanged)
        self.bt_reset.setEnabled(False)
        self.bt_clean.clicked.connect(self.clean)
        self.bt_autogen.clicked.connect(self.autogen)
        for name in self.servicePattern.getNamesByCategory("STATIC"):
            self.cb_staticPattern.addItem(name[1], name[0])
        self.cb_staticPattern.activated.connect(self.defineStaticPattern)
        for name in self.servicePattern.getNamesByCategory("PERIODIC"):
            self.cb_periodicPattern.addItem(name[1], name[0])
        self.cb_periodicPattern.activated.connect(self.definePeriodicPattern)
        for name in self.servicePattern.getNamesByCategory("MOVING"):
            self.cb_movingPattern.addItem(name[1], name[0])
        self.cb_movingPattern.activated.connect(self.defineMovingPattern)
        self.sb_xcell.setValue(self.config.x_cell)
        self.sb_xcell.valueChanged.connect(lambda: self.bt_reset.setEnabled(True))
        self.sb_ycell.setValue(self.config.y_cell)
        self.sb_ycell.valueChanged.connect(lambda: self.bt_reset.setEnabled(True))
        self.sb_sizecell.setValue(self.config.size_cell)
        self.sb_sizecell.valueChanged.connect(self.onSizeCellChange)
        self.sl_speed.setValue(self.config.speed)
        self.sl_speed.valueChanged.connect(self.onSpeedChange)

        self.timer = QTimer()
        self.timer.setInterval(self.config.speed)
        self.timer.timeout.connect(self.nextgen)
        self.timer.start()
        self.show()
        logger.info("Fin initialisation de la fenêtre principale.")

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

    def onSpeedChange(self):
        self.config.speed = self.sl_speed.value()
        self.timer.setInterval(self.sl_speed.value())
        logger.info("onSpeedChange : set refresh to :"+str(self.config.speed)+"ms")

    def onConfigChanged(self):
        if self.config.x_cell != self.sb_xcell.value() or self.config.y_cell != self.sb_ycell.value():
            self.config.x_cell = self.sb_xcell.value()
            self.config.y_cell = self.sb_ycell.value()
            self.lcd_generation.display(0)
            self.initBoard()
            logger.info("onConfigChanged : reset sreen size, redraw scene : X=" + str(self.config.x_cell) + " Y="+ str(self.config.y_cell))
        self.bt_reset.setEnabled(False)

    def autogen(self):
        self.board.autogen()
        self.scene.refreshScene()
        self.lcd_generation.display(0)
        logger.info("autogen : randow cell creation on board")

    def nextgen(self):
        if self.start:
            self.board.nextgen()
            self.scene.refreshScene()
            self.lcd_generation.display(self.lcd_generation.intValue() + 1)
            logger.debug("nextgen : calculate next generation et refresh the scene")


    def keyPressEvent(self, event):
        logger.info("keyPressEvent : pressed on : "+str(event.key()))
        if event.key() == Qt.Key_P:
            self.toggle_start()
        if event.key() == Qt.Key_A:
            self.autogen()
        if event.key() == Qt.Key_B:
            self.scene.clean()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.close()

    def initBoard(self):
        self.board = Board(self.config.x_cell, self.config.y_cell, self.config.density)
        self.scene = GolGraphicScene(self.board, self.config)
        self.configScene()
        self.scene.refreshScene()
        logger.info("initBoard : initialize board and draw scene")

    def initPreview(self):
        self.scenePreview = QGraphicsScene()
        self.scenePreview.setBackgroundBrush(self.config.inactive_color)
        self.gv_preview.setScene(self.scenePreview)
        logger.info("initPreview : initialize preview pattern scene")

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

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
