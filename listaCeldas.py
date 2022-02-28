from nodoCelda import Celda

class listaCeldas:
    def __init__(self,):
        self.primero = None
        self.ultimo = None
        self.size = 0 

    def insertarAlFinal(self, f, c, color, i):
        nuevaCelda = Celda(f, c, color, i)
        self.size += 1
        if self.primero == None:
            self.primero = nuevaCelda
            self.ultimo = nuevaCelda
        
        else:
            self.ultimo.setSiguiente(nuevaCelda)
            nuevaCelda.setAnterior(self.ultimo)
            self.ultimo = nuevaCelda
    #i representa la posición de la letra a la que hace referencia el nodo en la cadena de texto inicial.

    def mostrarCeldas(self):
        tmp = self.primero
        while tmp.siguiente != None:
            print("(" + tmp.fila + "," + tmp.columna + ") - > " + tmp.color)
            tmp = tmp.siguiente