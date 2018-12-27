# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fibonacci.ui'
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
        Dialog.resize(600, 413)
        self.labelTitulo = QtGui.QLabel(Dialog)
        self.labelTitulo.setGeometry(QtCore.QRect(40, 60, 181, 17))
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.lineNumero = QtGui.QLineEdit(Dialog)
        self.lineNumero.setGeometry(QtCore.QRect(230, 50, 113, 29))
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.ButtonCalcular = QtGui.QPushButton(Dialog)
        self.ButtonCalcular.setGeometry(QtCore.QRect(150, 120, 88, 29))
        self.ButtonCalcular.setObjectName(_fromUtf8("ButtonCalcular"))
        self.labelFibonacci = QtGui.QLabel(Dialog)
        self.labelFibonacci.setGeometry(QtCore.QRect(20, 210, 551, 51))
        self.labelFibonacci.setObjectName(_fromUtf8("labelFibonacci"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelTitulo.setText(_translate("Dialog", "Ingresa un numero : ", None))
        self.ButtonCalcular.setText(_translate("Dialog", "Calcular", None))
        self.labelFibonacci.setText(_translate("Dialog", "Serie Fibonacci: ", None))

