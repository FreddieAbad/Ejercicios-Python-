import sys
from sumaConversion import *

class MiFormulario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		#creo instancia de uidialog
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.ButtonCalcular, QtCore.SIGNAL('clicked()'),self.mostrarsuma)


	def mostrarsuma(self):
		if len(self.ui.lineNum1.text())!=0:
			a=int(self.ui.lineNum1.text())
		else:
			a=0
		if len(self.ui.lineNum2.text())!=0:
			b=int(self.ui.lineNum2.text())
		else:
			b=0
		sum=a+b
		self.ui.labelResultado.setText("Suma: "+str(sum))
		

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	myapp=MiFormulario()
	myapp.show()
	#loop de eventos hasta que se cierre la ventana
	sys.exit(app.exec_())