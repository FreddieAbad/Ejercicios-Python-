import sys
from fibonacci import *

class MiFormulario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		#creo instancia de uidialog
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.ButtonCalcular, QtCore.SIGNAL('clicked()'),self.fibonacci)


	def fibonacci(self):
		if len(self.ui.lineNumero.text())!=0:
			a=int(self.ui.lineNumero.text())
		else:
			a=0
		numero=1
		ultimo=0
		penultimo=0
		for contador in range(0,a):
			self.ui.labelFibonacci.setText("S. Fibonacci: "+str(numero))
			penultimo=ultimo
			ultimo=numero
			numero=penultimo+ultimo

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	myapp=MiFormulario()
	myapp.show()
	#loop de eventos hasta que se cierre la ventana
	sys.exit(app.exec_())