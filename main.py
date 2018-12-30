from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt, QPen, QTimer
from ui.mainwindow import Ui_MainWindow
from service.Board import Board
from ui.GolGraphicScene import GolGraphicScene
from service.UserContext import UserContext
from service.PatternFactory import PatternFactory



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.config = UserContext()
        self.patternFactory = PatternFactory()

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
        self.bt_clean.clicked.connect(self.clean)
        self.bt_autogen.clicked.connect(self.autogen)
        for name in self.patternFactory.staticPatterns.keys():
            self.cb_staticPattern.addItem(name)
        self.cb_staticPattern.activated.connect(lambda : self.scene.setPattern(self.patternFactory.staticPatterns[self.cb_staticPattern.currentText()]))
        for name in self.patternFactory.periodicPatterns.keys():
            self.cb_periodicPattern.addItem(name)
        self.cb_periodicPattern.activated.connect(lambda : self.scene.setPattern(self.patternFactory.periodicPatterns[self.cb_periodicPattern.currentText()]))
        for name in self.patternFactory.movingPatterns.keys():
            self.cb_movingPattern.addItem(name)
        self.cb_movingPattern.activated.connect(lambda : self.scene.setPattern(self.patternFactory.movingPatterns[self.cb_movingPattern.currentText()]))
        self.sb_xcell.setValue(self.config.x_cell)
        self.sb_ycell.setValue(self.config.y_cell)
        self.sb_sizecell.setValue(self.config.size_cell)
        self.sb_sizecell.valueChanged.connect(self.onSizeCellChange)
        self.sl_speed.setValue(self.config.speed)
        self.sl_speed.valueChanged.connect(self.onSpeedChange)

        self.timer = QTimer()
        self.timer.setInterval(self.config.speed)
        self.timer.timeout.connect(self.nextgen)
        self.timer.start()
        self.show()

    def toggle_start(self):
        pen = QPen(Qt.red)
        pen.setWidth(10)
        if self.start:
            self.start = False
            self.rect_statut = self.scene.addRect(0,0,self.config.x_cell*self.config.size_cell,self.config.y_cell*self.config.size_cell,pen)
        else:
            self.start = True
            self.scene.removeItem(self.rect_statut)

    def close(self):
        origin_state = self.start
        self.start = False
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Question?")
        msgBox.setText("Do you want to quit?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            QApplication.quit()
        else:
            self.start = origin_state

    def clean(self):
        self.scene.clean()
        self.lcd_generation.display(0)

    def onSizeCellChange(self):
        self.config.size_cell = self.sb_sizecell.value()
        self.scene = GolGraphicScene(self.board, self.config)
        if self.rect_statut:
            self.rect_statut.setRect(0,0,self.config.x_cell*self.config.size_cell,self.config.y_cell*self.config.size_cell)
        self.configScene()

    def onSpeedChange(self):
        self.config.speed = self.sl_speed.value()
        self.timer.setInterval(self.sl_speed.value())

    def onConfigChanged(self):
        if self.config.x_cell != self.sb_xcell.value() or self.config.y_cell != self.sb_ycell.value():
            self.config.x_cell = self.sb_xcell.value()
            self.config.y_cell = self.sb_ycell.value()
            self.lcd_generation.display(0)
            self.initBoard()

    def autogen(self):
        self.board.autogen()
        self.scene.refreshScene()
        self.lcd_generation.display(0)

    def nextgen(self):
        if self.start:
            self.board.nextgen()
            self.scene.refreshScene()
            self.lcd_generation.display(self.lcd_generation.intValue() + 1)


    def keyPressEvent(self, event):
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

    def initPreview(self):
        self.scenePreview = QGraphicsScene()
        self.scenePreview.setBackgroundBrush(self.config.inactive_color)
        self.gv_preview.setScene(self.scenePreview)

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

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
