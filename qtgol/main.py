from PyQt5.QtWidgets import *
from qtgol.ui.MainApp import MainApp
from qtgol.util.Log import Log

logger = Log().getLogger(__name__)

if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    app.exec_()
