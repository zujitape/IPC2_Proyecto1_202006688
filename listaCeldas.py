from nodoCelda import Celda
from graphviz import Digraph, dot
from os import startfile, system

class listaCeldas:
    def __init__(self,):
        self.primero = None
        self.ultimo = None
        self.size = 0 

    def insertarAlFinal(self, f, c, color):
        nuevaCelda = Celda(f, c, color)
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
        for i in range(self.size):
            print("(",tmp.fila, ",", tmp.columna, ") - > ", tmp.color)
            tmp = tmp.siguiente

    def reporte(self, patron):
        name = "graphviz"
        with open(name + ".dot", "w") as dot:
            dot.write('digraph Patrón de piso{\n')


        startfile("graphviz.png")
        startfile("graphviz.pdf")

    