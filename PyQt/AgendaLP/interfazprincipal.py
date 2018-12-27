# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        Dialog.resize(769, 595)
        self.ButtonAgregar = QtGui.QPushButton(Dialog)
        self.ButtonAgregar.setGeometry(QtCore.QRect(200, 50, 88, 29))
        self.ButtonAgregar.setObjectName(_fromUtf8("ButtonAgregar"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 113, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 113, 29))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 110, 113, 29))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 40, 113, 29))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.ButtonBuscar = QtGui.QPushButton(Dialog)
        self.ButtonBuscar.setGeometry(QtCore.QRect(600, 30, 88, 29))
        self.ButtonBuscar.setObjectName(_fromUtf8("ButtonBuscar"))
        self.ButtonEliminar = QtGui.QPushButton(Dialog)
        self.ButtonEliminar.setGeometry(QtCore.QRect(600, 70, 88, 29))
        self.ButtonEliminar.setObjectName(_fromUtf8("ButtonEliminar"))
        self.labelAgregar1 = QtGui.QLabel(Dialog)
        self.labelAgregar1.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.labelAgregar1.setObjectName(_fromUtf8("labelAgregar1"))
        self.labelAgregar2 = QtGui.QLabel(Dialog)
        self.labelAgregar2.setGeometry(QtCore.QRect(210, 90, 101, 31))
        self.labelAgregar2.setObjectName(_fromUtf8("labelAgregar2"))
        self.labelCI = QtGui.QLabel(Dialog)
        self.labelCI.setGeometry(QtCore.QRect(370, 20, 71, 17))
        self.labelCI.setObjectName(_fromUtf8("labelCI"))
        self.labelAE = QtGui.QLabel(Dialog)
        self.labelAE.setGeometry(QtCore.QRect(450, 100, 231, 71))
        self.labelAE.setObjectName(_fromUtf8("labelAE"))
        self.ButtonListar = QtGui.QPushButton(Dialog)
        self.ButtonListar.setGeometry(QtCore.QRect(300, 190, 131, 29))
        self.ButtonListar.setObjectName(_fromUtf8("ButtonListar"))
        self.tableViewListado = QtGui.QTableView(Dialog)
        self.tableViewListado.setGeometry(QtCore.QRect(30, 270, 711, 192))
        self.tableViewListado.setObjectName(_fromUtf8("tableViewListado"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Agenda", "Agenda", None))
        self.ButtonAgregar.setText(_translate("Dialog", "Agregar", None))
        self.ButtonBuscar.setText(_translate("Dialog", "Buscar", None))
        self.ButtonEliminar.setText(_translate("Dialog", "Eliminar", None))
        self.labelAgregar1.setText(_translate("Dialog", "AGREGAR >>", None))
        self.labelAgregar2.setText(_translate("Dialog", "USUARIO", None))
        self.labelCI.setText(_translate("Dialog", "CEDULA>>", None))
        self.labelAE.setText(_translate("Dialog", "USUARIO", None))
        self.ButtonListar.setText(_translate("Dialog", "Listar Usuarios", None))

