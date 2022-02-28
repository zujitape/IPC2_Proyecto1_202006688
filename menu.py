from tkinter.filedialog import askopenfilename
import pathlib
from xml.dom import minidom
from listaPisos import listaPisos

ListaPisos = listaPisos()

class Menu():
    def __init__(self):
        pass

def seleccionarOpt():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("¿Qué acción desea realizar?   "))
            correcto=True
        except ValueError:
            print('Asegúrese de seleccionar una opción correcta.')
    return num

def getFirst(char, data):
    element = data.getElementsByTagName(char)
    for e in element:
        newElement = e.firstChild.data
    return newElement

def MiniDom(ruta):
    mydoc = minidom.parse(ruta)
    piso = mydoc.getElementsByTagName('piso')
    for p in piso:
        nombre = p.attributes['nombre'].value
        nC = getFirst('C', p)
        nF = getFirst('R', p)
        pS = float(getFirst('S', p))
        pF = float(getFirst('F', p))
        
        nuevoPiso = ListaPisos.insertarPiso(nombre, nF, nC, pS, pF)
        
        print(' \nSe insertó el piso ',nuevoPiso.getNombre())

        patrones = p.getElementsByTagName('patron')
        for patron in patrones:
            cod = patron.attributes['codigo'].value
            cadena = patron.firstChild.data
            nuevoPiso.patrones.insertarPatron(cod, cadena)

        nuevoPiso.patrones.mostrarPatrones()


salir = False
opcion = 0

while not salir:
    print('')
    print('¡BIENVENIDO! \n 1. Cargar archivo. \n 2. Manejo de pisos. \n 3. Salir')

    opcion = seleccionarOpt()

    if opcion == 1:
        print("\n .:*・°☆ *:. CARGAR LISTA DE PISOS *・°☆.。.:")
        data = askopenfilename()
        path = pathlib.Path(data)
        if (path.suffix == '.xml'):
            codigo = MiniDom(data)

        else:
            print('ERROR: Seleccionó un tipo de archivo no permitido.')
        
    elif opcion == 2:
            print("Lista de pisos disponibles: ")
        #Mostar lista de pisos disponibles, + ¿Cuál manejará?
            ListaPisos.mostrarPisos()
            numMaximo = ListaPisos.size
            print(numMaximo)
            

    elif opcion == 3:
        salir = True
    else:
        print ("Asegúrate de ingresar una opción correcta.")
        


    