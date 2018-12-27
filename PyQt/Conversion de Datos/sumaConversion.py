# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumaConversion.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(567, 369)
        self.labelNum1 = QtGui.QLabel(Dialog)
        self.labelNum1.setGeometry(QtCore.QRect(90, 50, 56, 17))
        self.labelNum1.setObjectName(_fromUtf8("labelNum1"))
        self.labelNum2 = QtGui.QLabel(Dialog)
        self.labelNum2.setGeometry(QtCore.QRect(90, 110, 56, 17))
        self.labelNum2.setObjectName(_fromUtf8("labelNum2"))
        self.labelResultado = QtGui.QLabel(Dialog)
        self.labelResultado.setGeometry(QtCore.QRect(90, 170, 381, 17))
        self.labelResultado.setObjectName(_fromUtf8("labelResultado"))
        self.lineNum1 = QtGui.QLineEdit(Dialog)
        self.lineNum1.setGeometry(QtCore.QRect(220, 50, 113, 29))
        self.lineNum1.setObjectName(_fromUtf8("lineNum1"))
        self.lineNum2 = QtGui.QLineEdit(Dialog)
        self.lineNum2.setGeometry(QtCore.QRect(220, 100, 113, 29))
        self.lineNum2.setObjectName(_fromUtf8("lineNum2"))
        self.ButtonCalcular = QtGui.QPushButton(Dialog)
        self.ButtonCalcular.setGeometry(QtCore.QRect(190, 230, 88, 29))
        self.ButtonCalcular.setObjectName(_fromUtf8("ButtonCalcular"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelNum1.setText(_translate("Dialog", "Numero 1 :", None))
        self.labelNum2.setText(_translate("Dialog", "Numero 2 : ", None))
        self.labelResultado.setText(_translate("Dialog", "Resultado", None))
        self.ButtonCalcular.setText(_translate("Dialog", "Sumar", None))

