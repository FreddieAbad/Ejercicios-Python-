# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bienvenido.ui'
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
        Dialog.resize(400, 300)
        self.labelEscribeNombre = QtGui.QLabel(Dialog)
        self.labelEscribeNombre.setGeometry(QtCore.QRect(30, 70, 56, 17))
        self.labelEscribeNombre.setObjectName(_fromUtf8("labelEscribeNombre"))
        self.labelMensaje = QtGui.QLabel(Dialog)
        self.labelMensaje.setGeometry(QtCore.QRect(80, 170, 211, 21))
        self.labelMensaje.setText(_fromUtf8(""))
        self.labelMensaje.setObjectName(_fromUtf8("labelMensaje"))
        self.Buttonpulsar = QtGui.QPushButton(Dialog)
        self.Buttonpulsar.setGeometry(QtCore.QRect(130, 120, 88, 29))
        self.Buttonpulsar.setObjectName(_fromUtf8("Buttonpulsar"))
        self.lineEditNombreUsuario = QtGui.QLineEdit(Dialog)
        self.lineEditNombreUsuario.setGeometry(QtCore.QRect(160, 60, 113, 29))
        self.lineEditNombreUsuario.setObjectName(_fromUtf8("lineEditNombreUsuario"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEscribeNombre.setText(_translate("Dialog", "Nombre:", None))
        self.Buttonpulsar.setText(_translate("Dialog", "Pulsar", None))

