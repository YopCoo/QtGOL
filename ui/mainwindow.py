# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/qtGol.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.canvas = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.canvas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionstart_pause = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("NewGui/media-playback-start-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstart_pause.setIcon(icon)
        self.actionstart_pause.setObjectName("actionstart_pause")
        self.actionSpeed = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("NewGui/media-seek-backward-symbolic-rtl.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeed.setIcon(icon1)
        self.actionSpeed.setObjectName("actionSpeed")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("NewGui/application-exit-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConfig = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("NewGui/system-run-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfig.setIcon(icon3)
        self.actionConfig.setObjectName("actionConfig")
        self.actionrefresh = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("asset/view-refresh-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrefresh.setIcon(icon4)
        self.actionrefresh.setObjectName("actionrefresh")
        self.toolBar.addAction(self.actionstart_pause)
        self.toolBar.addAction(self.actionrefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSpeed)
        self.toolBar.addAction(self.actionConfig)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionstart_pause.setText(_translate("MainWindow", "start/pause"))
        self.actionSpeed.setText(_translate("MainWindow", "Speed"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.actionrefresh.setText(_translate("MainWindow", "refresh"))

