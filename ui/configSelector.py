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
        Dialog.resize(284, 166)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
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
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lb_xcell = QtWidgets.QLabel(Dialog)
        self.lb_xcell.setObjectName("lb_xcell")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_xcell)
        self.sb_xcell = QtWidgets.QSpinBox(Dialog)
        self.sb_xcell.setObjectName("sb_xcell")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sb_xcell)
        self.lb_ycell = QtWidgets.QLabel(Dialog)
        self.lb_ycell.setObjectName("lb_ycell")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_ycell)
        self.sb_ycell = QtWidgets.QSpinBox(Dialog)
        self.sb_ycell.setObjectName("sb_ycell")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sb_ycell)
        self.lb_sizecell = QtWidgets.QLabel(Dialog)
        self.lb_sizecell.setObjectName("lb_sizecell")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_sizecell)
        self.sb_sizecell = QtWidgets.QSpinBox(Dialog)
        self.sb_sizecell.setObjectName("sb_sizecell")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sb_sizecell)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_defaut = QtWidgets.QPushButton(Dialog)
        self.btn_defaut.setObjectName("btn_defaut")
        self.horizontalLayout_2.addWidget(self.btn_defaut)
        self.btn_accept = QtWidgets.QPushButton(Dialog)
        self.btn_accept.setObjectName("btn_accept")
        self.horizontalLayout_2.addWidget(self.btn_accept)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_newcolor.setText(_translate("Dialog", "New Color"))
        self.btn_activecolor.setText(_translate("Dialog", "Active Color"))
        self.btn_inactivecolor.setText(_translate("Dialog", "Inactive Color"))
        self.lb_xcell.setText(_translate("Dialog", "X Cell"))
        self.lb_ycell.setText(_translate("Dialog", "Y Cell"))
        self.lb_sizecell.setText(_translate("Dialog", "Size Cell"))
        self.btn_defaut.setText(_translate("Dialog", "Defaut"))
        self.btn_accept.setText(_translate("Dialog", "OK"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))

