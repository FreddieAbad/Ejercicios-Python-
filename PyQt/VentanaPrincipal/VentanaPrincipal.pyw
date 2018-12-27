import sys
from PyQt4.QtWidget import QApplication, QMainWindow
from PyQt4 import uic

#clase heradada de qmainwindow (constructro de ventana)
class Ventana(QMainWindow):
	def __init__(self):
		#inicio ojeto de qmainwindow
		QMainWindow.__init__(self)
		#cargar la cofiguracion de archivo.ui en objeto
		uic.loadUi("Ventana Principal.ui",self)

#instancia para iniciar app
app=QApplication(sys.argv)
#creo objeto de clase ventana
_ventana=Ventana()
_ventana.show()
#ejecuto la app
app.exec_()