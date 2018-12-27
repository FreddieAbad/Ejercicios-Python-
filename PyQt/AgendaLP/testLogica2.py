listaNombre=[]
listaApellido=[]
listaCI=[]

def menu():
	print ("bienvenidos a la agenda virtual")
	print ("1.nombre")
	print ("2.apellidos")
	print ("3.CI")
	print ("4.VER DATOS")
	print ("5.salir")
def nombre():
	a=raw_input("ingrese su nombre:")
	listaNombre.append(a)
	'nombre:'.join(a)
def apellido():
	b=raw_input("ingrese su apellido:")
	listaApellido.append(b)
	'nombre:'.join(b)
def CI():
	c=raw_input("ingrese su CI:")
	listaCI.append(c)
	'nombre:'.join(c)
def ver_datos():
	print (listaNombre)
	print (listaApellido)
	print (listaCI)
def agenda():
	while 1:
		menu()
		op=input("ingrese opcion:")
		if op==1:
			nombre()
		if op==2:
			apellido()
		if op==3:
			CI()
		if op==4:
			ver_datos()

agenda()