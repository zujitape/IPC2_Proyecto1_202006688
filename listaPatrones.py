from nodoPatron import Patron

class listaPatrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0 

    def insertarPatron(self, cod, patron):
        nuevoPatron = Patron(cod, patron)
        self.size += 1
        if self.primero is None:
            self.primero = nuevoPatron
            self.ultimo = nuevoPatron
        else:
            self.ultimo.setSiguiente(nuevoPatron)
            self.ultimo = nuevoPatron   
        return nuevoPatron

    def buscarPatron(self, c):
        tmp = self.primero
        while tmp is not None:
            if tmp.cod == c:
                return tmp
            tmp = tmp.getSiguiente()

    def size(self):
        return self.size
        
    def mostrarPatrones(self):
        tmp = self.primero
        for i in range(self.size):
            print("Patrón ",(i+1),": ", tmp.getCodigo(), " - ", tmp.getPatron())
            tmp = tmp.getSiguiente()
    
    def diferenteChar(self, patronDestino):
        patronInicial = self.primero.getPatron()
        for i in patronInicial:
            if patronInicial[i] != patronDestino[i]:
                index = patronInicial.index()
        return index
    