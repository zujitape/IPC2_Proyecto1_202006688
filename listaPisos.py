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
            print((i+1), ". ", tmp.getNombre(), '; número de patrones disponibles: ', str(tmp.patrones.size))
            tmp = tmp.getSiguiente()
        
    def buscarPiso(self, name):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == name:
                return tmp
            tmp = tmp.getSiguiente()
    