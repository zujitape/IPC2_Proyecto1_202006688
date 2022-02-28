from xml.dom import minidom
from listaPisos import listaPisos

ListaPisos = listaPisos()

class cargarPisos:
    def __init__(self):
        pass

    def MiniDom(ruta):
        mydoc = minidom.parse(ruta)
        piso = mydoc.getElementsByTagName('piso')
        for p in piso:
            nombre = p.attributes['nombre'].value
            nC = cargarPisos.getFirst('C', p)
            nF = cargarPisos.getFirst('R', p)
            pS = float(cargarPisos.getFirst('S', p))
            pF = float(cargarPisos.getFirst('F', p))
            
            nuevoPiso = ListaPisos.insertarPiso(nombre, nF, nC, pS, pF)
            
            print(' \nSe insertó el piso ',nuevoPiso.getNombre())

            patrones = p.getElementsByTagName('patron')
            for patron in patrones:
                cod = patron.attributes['codigo'].value
                cadena = patron.firstChild.data
                nuevoPiso.patrones.insertarPatron(cod, cadena)

            nuevoPiso.patrones.mostrarPatrones()

    def getFirst(char, data):
        element = data.getElementsByTagName(char)
        for e in element:
            newElement = e.firstChild.data
        return newElement
        