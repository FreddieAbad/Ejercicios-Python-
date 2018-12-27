import sys
from bienvenido import *

class MiFormulario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		#creo instancia de uidialog
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.Buttonpulsar, QtCore.SIGNAL('clicked()'),self.mostrarmensaje)


	def mostrarmensaje(self):
		self.ui.labelMensaje.setText("Hola "+self.ui.lineEditNombreUsuario.text())


if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	myapp=MiFormulario()
	myapp.show()
	#loop de eventos hasta que se cierre la ventana
	sys.exit(app.exec_())