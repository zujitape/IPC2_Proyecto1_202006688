class Celda():
    def __init__(self, fila, columna, color):
        self.fila = fila 
        self.columna = columna 
        self.color = color 
        self.siguiente = None
        self.anterior = None

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, celda):
        self.siguiente = celda

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, celda):
        self.anterior = celda
    
    def getColor(self):
        return self.color

    def getFila(self):
        return self.fila
    
    def getRow(self):
        return self.columna

    def setColor(self, color):
        self.color = color