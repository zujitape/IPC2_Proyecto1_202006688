from nodoPiso import Piso

class listaPisos():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertarPiso(self, nombre, nF, nC, cF, cS):
        nuevoPiso = Piso(nombre, nF, nC, cF, cS)
        self.size += 1
        if self.primero is None:
            self.primero = nuevoPiso
            self.ultimo = nuevoPiso
        else:
            self.ultimo.setSiguiente(nuevoPiso)
            self.ultimo = nuevoPiso   
        return nuevoPiso

    def mostrarPisos(self):
        tmp = self.primero
        for i in range(self.size):
            print(i, 'Nombre:', tmp.getNombre(), 'Patrones: ', tmp.getPatron())
            tmp = tmp.getSiguiente()