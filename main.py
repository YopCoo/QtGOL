from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt, QPen, QTimer
from mainwindow import Ui_MainWindow
from Board import Board
from GolGraphicScene import GolGraphicScene
from UserContext import UserContext
from StateCell import StateCell


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.config = UserContext()
        self._x_cell = self.config.x_cell
        self._y_cell = self.config.y_cell
        self._density = self.config.density
        self._size_cell = self.config.size_cell
        self._speed = self.config.speed

        self.start = False
        self.board = None
        self.rect_statut = None

        self.setupUi(self)
        self.scene = None

        self.initBoard(self.config)

        self.bt_quit.clicked.connect(self.close)
        self.bt_start.clicked.connect(self.toggle_start)
        self.bt_reset.clicked.connect(self.reset)
        self.bt_clean.clicked.connect(self.clean)
        self.bt_autogen.clicked.connect(self.autogen)

        self.sb_xcell.setValue(self._x_cell)
        self.sb_ycell.setValue(self._y_cell)
        self.sb_sizecell.setValue(self._size_cell)
        self.sb_sizecell.valueChanged.connect(self.onSizeChange)
        self.sl_speed.setValue(self._speed)


        self.timer = QTimer()
        self.timer.setInterval(self._speed)
        self.timer.timeout.connect(self.nextgen)
        self.timer.start()
        self.show()

    def refresh(self):
        for cell in self.board.cells:
            if cell.state == StateCell.LIFE:
                self.scene.setActiveCell(cell.c_x,cell.c_y)
            elif cell.state == StateCell.BORN:
                self.scene.setNewCell(cell.c_x,cell.c_y)
            elif cell.state == StateCell.DEATH:
                self.scene.setInativeCell(cell.c_x, cell.c_y)

    def toggle_start(self):
        pen = QPen(Qt.red)
        pen.setWidth(10)
        if self.start:
            self.start = False
            self.rect_statut = self.scene.addRect(0,0,self._x_cell*self.config.size_cell,self._y_cell*self.config.size_cell,pen)
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
        for cell in self.board.cells:
            cell.state = False
            self.scene.setInativeCell(cell.c_x, cell.c_y)

    def reset(self):
        self.loadConfigChanged()

    def onSizeChange(self):
        self.config.size_cell = self.sb_sizecell.value()
        self._size_cell = self.config.size_cell
        self.scene = GolGraphicScene(self.board, self.config)
        self.scene.setBackgroundBrush(self.config.inactive_color)
        self.canvas.setScene(self.scene)
        if self.start == False:
            pen = QPen(Qt.red)
            pen.setWidth(10)
            self.rect_statut = self.scene.addRect(0, 0, self._x_cell * self._size_cell,
                                                  self._y_cell * self._size_cell, pen)
        self.canvas.setFixedWidth(self._x_cell * self._size_cell)
        self.canvas.setFixedHeight(self._y_cell * self._size_cell)

    def autogen(self):
        self.board.autogen()
        self.refresh()

    def nextgen(self):
        if self.start:
            self.board.nextgen()
            self.refresh()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.toggle_start()
        if event.key() == Qt.Key_A:
            self.autogen()
        if event.key() == Qt.Key_B:
            self.clean()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.close()

    def loadConfigChanged(self):
        if self._x_cell != self.sb_xcell.value() or self._y_cell != self.sb_ycell.value():
            self._x_cell = self.sb_xcell.value()
            self._y_cell = self.sb_ycell.value()
            self.initBoard(self.config)

    def initBoard(self, config):
        self.board = Board(self._x_cell, self._y_cell, self._density)
        self.scene = GolGraphicScene(self.board, config)
        self.scene.setBackgroundBrush(self.config.inactive_color)
        if self.start == False:
            pen = QPen(Qt.red)
            pen.setWidth(10)
            self.rect_statut = self.scene.addRect(0, 0, self._x_cell * self._size_cell,
                                                  self._y_cell * self._size_cell, pen)
        self.canvas.setScene(self.scene)
        self.canvas.setFixedWidth(self._x_cell * self._size_cell)
        self.canvas.setFixedHeight(self._y_cell * self._size_cell)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
