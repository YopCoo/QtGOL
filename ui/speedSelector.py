# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/speedSelector.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(109, 84)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ind_speed = QtWidgets.QLabel(Dialog)
        self.ind_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.ind_speed.setObjectName("ind_speed")
        self.verticalLayout.addWidget(self.ind_speed)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_lower = QtWidgets.QToolButton(Dialog)
        self.btn_lower.setObjectName("btn_lower")
        self.horizontalLayout.addWidget(self.btn_lower)
        self.btn_upper = QtWidgets.QToolButton(Dialog)
        self.btn_upper.setObjectName("btn_upper")
        self.horizontalLayout.addWidget(self.btn_upper)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Speed Selector"))
        self.ind_speed.setText(_translate("Dialog", "X gen / sec"))
        self.btn_lower.setText(_translate("Dialog", "-"))
        self.btn_upper.setText(_translate("Dialog", "+"))

