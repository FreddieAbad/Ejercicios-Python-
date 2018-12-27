import sys



mantenimiento=[]   #lista para el mantenimiento

#ingresar los datos a la lista
def ingresar(mantenimiento):
    
    numC=int(input("Ingrese el valor  de su cedula:"))
    nombre=(input("Ingrese el nombre:"))
    apellido=(input("Ingrese el apellido:"))
    print("La cedula ingresado es : ",numC)
    print("El nombre ingresado es: ",nombre)
    print("El apeliido ingresado es: ",apellido)
    
    mantenimiento.append(numC)
    mantenimiento.append(nombre)
    mantenimiento.append(apellido)
    
    
    return mantenimiento
    

def editar(mantenimiento):
    
    ced=int(input("Ingrese la cedula de la persona que quiere editar sus datos: "))
    pos=mantenimiento.index(ced)
    nombre=input("Ingrese el nuevo nombre: ")
    apellido=input("Ingrese el nuevo apellido: ")
    
    mantenimiento[pos+1]=nombre
    mantenimiento[pos+2]=apellido
   # mantenimiento.insert(pos+1,nombre)
    #mantenimiento.insert(pos+2,apellido)

def eliminar(mantenimiento):
    
    num=len(mantenimiento)
   # print(num)
    if num!=0:
       # print(mantenimiento)
        ced=int(input("Ingrese la cedula de la persona que desea eliminar sus datos: "))
        busco= ced in mantenimiento
        if busco==True:
            posicion= mantenimiento.index(ced)    #encuentra la posicion de la cedula
           # print(posicion)
            ced=mantenimiento[posicion]    #extrae los valores correspondientes
            nom=mantenimiento[posicion+1]
            ape=mantenimiento[posicion+2]
            mantenimiento.remove(ced)   #remove de la lista dichos valores anteriores
            mantenimiento.remove(nom)
            mantenimiento.remove(ape)

    else:
        print("No existe elementos en la lista consultada")

def mostrar(mantenimiento):
    
    if len(mantenimiento)!=0:
        print(mantenimiento)
    else:
        print("No se han ingresado valores")    

def buscar(mantenimiento):
    
    ced=int(input("Ingrese la cedula de la persona que desea eliminar sus datos: "))
    busco= ced in mantenimiento
    
    if(busco==True):
        posicion= mantenimiento.index(ced)    #encuentra la posicion de la cedula
        # print(posicion)
        cedu=mantenimiento[posicion]    #extrae los valores correspondientes
        nom=mantenimiento[posicion+1]
        ape=mantenimiento[posicion+2]
        print("DATOS ENCONTRADOS")
        print("Cedula: ",cedu)
        print("Nombre: ",nom)
        print("Apellido:",ape)
    
    else:
        print("NO SE HA ENCONTRADO A ESA PERSONA CON ESE NUMERO DE CEDULA")   


print("MANTENIMIENTO DE DATOS")
  
op=0 
 
while op!=6:
    print("1.Ingresar datos")
    print("2.Mostrar datos")
    print("3.Eiminar datos")
    print("4.Editar datos")
    print("5.Buscar")
    print ("6.Salir")
    op=int(input("Seleccione una opcion: "))
    
    if op==1:
        ingresar(mantenimiento)
      
    elif op==2:
         mostrar(mantenimiento)
      
    elif op==3:
        eliminar(mantenimiento)
        
    elif op==4:
         editar(mantenimiento)
       
    elif op==5:
         buscar(mantenimiento)
         
   
             
       