from tkinter.filedialog import askopenfilename
import pathlib
import os, sys, time
from xml.dom import minidom
from listaPisos import listaPisos

ListaPisos = listaPisos()

class Menu():
    def __init__(self):
        pass

def seleccionarOpt(salida):
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(salida))
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

    #insertar pisos:
    piso = mydoc.getElementsByTagName('piso')
    for p in piso:
        nombre = p.attributes['nombre'].value
        nC = int(getFirst('C', p))
        nF = int(getFirst('R', p))
        pS = float(getFirst('S', p))
        pF = float(getFirst('F', p))
        
        nuevoPiso = ListaPisos.insertarPiso(nombre, nF, nC, pS, pF)
        
        print(' \nSe insertó el piso ',nuevoPiso.getNombre())

    #insertar patrones:
        patrones = p.getElementsByTagName('patron')
        for patron in patrones:
            cod = patron.attributes['codigo'].value
            cadena = patron.firstChild.data
            nuevoPiso.patrones.insertarPatron(cod, cadena)
    
    #insertar celdas:

        nuevoPiso.patrones.mostrarPatrones()

        cadenaI = p.getElementsByTagName("patron")[0]
        cadenaI = cadenaI.firstChild.data
             
        iFila = 1
        iColumna = 1
        maxColumnas = nC
        i = 0
        while i <len(cadenaI):
            if iColumna <= maxColumnas:
                nuevoPiso.celdas.insertarAlFinal(iFila, iColumna, cadenaI[i])
                iColumna += 1
                i += 1
            else:
                iFila += 1
                iColumna = 1

salir = False
opcion = 0

salirPisos = False
optPiso = 0

while not salir:
    print('')
    print('¡BIENVENIDO! \n 1. Cargar archivo. \n 2. Mostrar pisos. \n 3. Ver piso. \n 4. Salir.')

    opcion = seleccionarOpt("¿Qué opción quiere seleccionar? ")

    if opcion == 1:
        print("\n .:*・°☆CARGAR LISTA DE PISOS☆.。.:")
        data = askopenfilename()
        path = pathlib.Path(data)
        if (path.suffix == '.xml'):
            codigo = MiniDom(data)

        else:
            print('ERROR: Seleccionó un tipo de archivo no permitido.')
        
    elif opcion == 2:
        try:
            print("\nLista de pisos disponibles: ")
            ListaPisos.mostrarPisos()
        except:
            print("¿Ya cargó un archivo al sistema?")

    elif opcion == 3:
            name = input("Ingrese el nombre del piso que manejará: ")
            piso = ListaPisos.buscarPiso(name)

            if piso == None:
                print("Asegúrese de que el nombre ingresado sea correcto.")
            
            else:
                print("\nPISO: ", piso.getNombre())
                piso.celdas.mostrarCeldas()


                print("\n 1. Cambiar patrones. \n 2. Imprimir patrón. \n 3. Regresar")
                optPiso = seleccionarOpt("\nSeleccione la acción que quiere realizar: ")
                

                while not salirPisos:
                    if optPiso == 1:
                        print("\nPISO: ", piso.getNombre())
                        piso.celdas.mostrarCeldas()
                        print("\nLos patrones disponibles para cambiar este piso, son: ")
                        piso.patrones.mostrarPatrones()

                        codigo = input("Cambiar piso al nuevo patrón de código: " )

                        piso.patrones.buscarPatron(codigo)

                    elif optPiso == 2:
                            print('\n' + piso.nombre)
                            piso.celdas.mostrarCeldas()
                            piso.celdas.reporte(piso.nColumnas, piso.nFilas, piso.nombre)
                            print("\nReporte generado correctamente!")
                            break

                        
                    elif optPiso == 3:
                        salirPisos = True
                    
                

    elif opcion == 4:
        print("Saliendo... :b")
        time.sleep(0.5)
        salir = True

    else:
        print ("Asegúrate de ingresar una opción correcta.")
        


    