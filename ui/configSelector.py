# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/configSelector.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 165)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lb_xcell = QtWidgets.QLabel(Dialog)
        self.lb_xcell.setObjectName("lb_xcell")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_xcell)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.lb_ycell = QtWidgets.QLabel(Dialog)
        self.lb_ycell.setObjectName("lb_ycell")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_ycell)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.lb_sizecell = QtWidgets.QLabel(Dialog)
        self.lb_sizecell.setObjectName("lb_sizecell")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_sizecell)
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_newcolor = QtWidgets.QPushButton(Dialog)
        self.btn_newcolor.setObjectName("btn_newcolor")
        self.horizontalLayout.addWidget(self.btn_newcolor)
        self.btn_activecolor = QtWidgets.QPushButton(Dialog)
        self.btn_activecolor.setObjectName("btn_activecolor")
        self.horizontalLayout.addWidget(self.btn_activecolor)
        self.btn_inactivecolor = QtWidgets.QPushButton(Dialog)
        self.btn_inactivecolor.setObjectName("btn_inactivecolor")
        self.horizontalLayout.addWidget(self.btn_inactivecolor)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_xcell.setText(_translate("Dialog", "X Cell"))
        self.lb_ycell.setText(_translate("Dialog", "Y Cell"))
        self.lb_sizecell.setText(_translate("Dialog", "Size Cell"))
        self.btn_newcolor.setText(_translate("Dialog", "New Color"))
        self.btn_activecolor.setText(_translate("Dialog", "Active Color"))
        self.btn_inactivecolor.setText(_translate("Dialog", "Inactive Color"))

