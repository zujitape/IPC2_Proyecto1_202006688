from listaCeldas import listaCeldas
from listaPatrones import listaPatrones

class Piso():
    def __init__(self, nombre, nFilas, nColumnas, costoFlip, costoSlide):
        self.nombre = nombre
        self.nFilas = nFilas
        self.nColumnas = nColumnas
        self.costoFlip = costoFlip
        self.costoSlide = costoSlide
        self.siguiente = None
        self.patrones = listaPatrones()
        self.celdas = listaCeldas() #

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, piso):
        self.siguiente = piso

    def getNombre(self):
        return self.nombre 
    
    def getPatron(self):
        return self.patrones 
    
#Jalar el primer elemento de la lista de patrones y con ese valor de color, asignarlo a una nueva celda que se cree.
