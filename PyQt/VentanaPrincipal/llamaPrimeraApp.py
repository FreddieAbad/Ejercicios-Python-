import sys
from tutotialQT.py import *

class MiFormulario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QtWidget.__init__(self,parent)
		#creo instancia de uidialog
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	myapp=MiFormulario()
	myapp.show()
	#loop de eventos hasta que se cierre la ventana
	sys.exit(app.exec_())