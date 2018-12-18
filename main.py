from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPen, QBrush
from mainwindow import Ui_MainWindow
from Board import Board
from GolGraphicScene import GolGraphicScene

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        pen = QPen(Qt.black)
        self.active_color = QBrush(Qt.yellow)
        self.active_color.setStyle(Qt.SolidPattern)
        self.inactive_color = QBrush()
        self.inactive_color.setStyle(0)

        self.start = False
        self.board = Board(10, 10, 0.3)
        self.pixels = {}

        self.setupUi(self)
        self.scene = GolGraphicScene(self.board)
        self.scene.setBackgroundBrush(Qt.gray)
        self.canvas.setScene(self.scene)
        self.canvas.setFixedWidth(60*10)
        self.canvas.setFixedHeight(60*10)
        for cell in self.board.cells:
            brush = self.active_color if cell.state else self.inactive_color
            self.pixels['#'+str(cell.c_x)+'#'+str(cell.c_y)] = self.scene.addRect(10*cell.c_x,10*cell.c_y,10,10, pen, brush)

        self.bt_quit.clicked.connect(self.close)
        self.bt_start.clicked.connect(self.toggle_start)
        self.timer = QTimer()
        self.timer.setInterval(150)
        self.timer.timeout.connect(self.refresh)
        self.timer.start()
        self.show()

    def refresh(self):
        if self.start:
            self.board.nextgen()
            for cell in self.board.cells:
                brush = self.active_color if cell.state else self.inactive_color
                self.pixels['#' + str(cell.c_x) + '#' + str(cell.c_y)].setBrush(brush)

    def toggle_start(self):
        self.start = False if self.start else True

    def toggle_cell(self, e):
        pass

    def close(self):
        origin_state = self.start
        self.start = False
        msgBox = QMessageBox()
        msgBox.setText("Question?")
        msgBox.setInformativeText("Do you want to quit?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            QApplication.quit()
        else:
            self.start = origin_state


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
