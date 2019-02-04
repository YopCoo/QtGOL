from PyQt5.QtWidgets import *
from ui.MainApp import MainApp
from util.Log import Log

logger = Log().getLogger(__name__)

if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    app.exec_()
