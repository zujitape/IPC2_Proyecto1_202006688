#nodoJavier?

class Patron():
    def __init__(self, codigo, patron):
        self.codigo = codigo
        self.patron = patron
        self.siguiente = None
    
    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, patron):
        self.siguiente = patron

    def getPatron(self):
        return self.patron 
    
    def getCodigo(self):
        return self.codigo 