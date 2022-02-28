from tkinter.filedialog import askopenfilename
import pathlib
from cargaPisos import cargarPisos

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

salir = False
opcion = 0

while not salir:
    print('')
    print('¡BIENVENIDO! \n 1. Cargar archivo. \n 2. Manejo de pisos. \n 4. Salir')

    opcion = seleccionarOpt()

    if opcion == 1:
        print("\n .:*・°☆ *:. CARGAR LISTA DE PISOS *・°☆.。.:")
        print('')
        data = askopenfilename()
        path = pathlib.Path(data)
        if (path.suffix == '.xml'):
            codigo = cargarPisos.MiniDom(data)
            codigo = cargarPisos.elementTree(data)
            
        
        else:
            print('ERROR: Seleccionó un tipo de archivo no permitido!')
    
    elif opcion == 4:
        salir = True

    else:
        print ("Asegúrate de ingresar una opción correcta.")
        


    