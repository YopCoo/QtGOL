from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPen, QBrush, QColor
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        pen = QPen()
        active_color = QBrush()
        active_color.setStyle(1)
        inactive_color = QBrush()
        inactive_color.setStyle(0)


        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.canvas.setScene(self.scene)
        self.scene.addRect(10, 10, 40, 30, pen, active_color)
        self.scene.addRect(5, 5, 50, 10, pen, inactive_color)
        self.bt_quit.clicked.connect(self.close)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.start()
        self.show()

    def initRect(self,x,y,w,h):
        pass
    def close(self):
        msgBox = QMessageBox()
        msgBox.setText("Question?")
        msgBox.setInformativeText("Do you want to quit?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
