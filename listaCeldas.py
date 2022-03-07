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

    def mostrarCeldas(self):
        tmp = self.primero
        for i in range(self.size):
            print("(",tmp.fila, ",", tmp.columna, ") - > ", tmp.color)
            tmp = tmp.siguiente

    def reporte(self, maxColumnas, maxFilas, name):
        iFila = 1
        iColumna = 1

        i=0
        nombre = "graphviz"
        with open(nombre + ".dot", "w") as dot:
            dot.write('digraph Piso{\n')
            dot.write('node[shape = box fillcolor="#FFEDBB" style = filled]\n')
            dot.write('nodesep=0.05; ranksep=0.05;subgraph cluster_p{\n')
            dot.write('label = "Patron inicial del piso '+ name + '"\nfontname="Impact"\nlabelloc="b"\nbgcolor = "#922B21"\n')
            dot.write('edge[dir = "none" style = invisible]\n')
            tmp = self.primero
            i = 1
            while tmp is not None:
                if tmp.color == 'B':
                    nColor = 'black'
                else:
                    nColor = 'white'
                    
                dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'[label = "", group ='+str(tmp.columna)+ ', fillcolor= '+ nColor +'] \n')
                i+=1

                tmp = tmp.siguiente
            

            #rank para las mismas filas:
            tmp = self.primero
            iFila = 1
            dot.write('{rank = same;') 

            while tmp is not None:
                if tmp.fila == iFila:
                    dot.write('columna'+ str(tmp.fila)+str(tmp.columna)+';')
                else:
                    iFila += 1
                    dot.write('}\n{rank = same; columna'+ str(tmp.fila)+str(tmp.columna)+';')

                tmp = tmp.siguiente
            
            dot.write('}\n')
            

            #Apuntadores por fila:
            tmp = self.primero  
            iFila = 1
            while tmp != None:
                if tmp.fila == iFila and tmp.columna < maxColumnas:
                    dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'->'+'columna'+str(tmp.fila)+str(tmp.columna+1)+';\n')
                else:
                    iFila += 1
                
                tmp = tmp.siguiente
                
            #Apuntadores para la primera columna:
            tmp = self.primero
            iColumna = 1
            while tmp is not None:
                if tmp.columna == iColumna and tmp.fila < maxFilas:
                    dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'->'+'columna'+str(tmp.fila+1)+str(tmp.columna)+';\n')
                else:
                    pass
                tmp = tmp.siguiente


            dot.write('}\n')
            dot.write('}')

        system("dot -Tpng graphviz.dot -o patronInicial.png")
        startfile("patronInicial.png")

    def reporteFinal(self, maxColumnas, maxFilas, name, cadena):
        iFila = 1
        iColumna = 1

        i=0
        nombre = "graphviz"
        with open(nombre + ".dot", "w") as dot:
            dot.write('digraph Piso{\n')
            dot.write('node[shape = box fillcolor="#FFEDBB" style = filled]\n')
            dot.write('nodesep=0.05; ranksep=0.05;subgraph cluster_p{\n')
            dot.write('label = "Patron final del piso '+ name + '"\nfontname="Impact"\nlabelloc="b"\nbgcolor = "#922B21"\n')
            dot.write('edge[dir = "none" style = invisible]\n')
            tmp = self.primero
            i = 1
            n = 0
            while tmp is not None:
                if tmp.color != cadena[n]:
                        tmp.color = cadena[n]
                else:
                    pass

                if tmp.color == 'B':
                    nColor = 'black'
                else:
                    nColor = 'white'
                    
                dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'[label = "", group ='+str(tmp.columna)+ ', fillcolor= '+ nColor +'] \n')
                i+=1
                n+=1

                tmp = tmp.siguiente
            

            #rank para las mismas filas:
            tmp = self.primero
            iFila = 1
            dot.write('{rank = same;') 

            while tmp is not None:
                if tmp.fila == iFila:
                    dot.write('columna'+ str(tmp.fila)+str(tmp.columna)+';')
                else:
                    iFila += 1
                    dot.write('}\n{rank = same; columna'+ str(tmp.fila)+str(tmp.columna)+';')

                tmp = tmp.siguiente
            
            dot.write('}\n')
            

            #Apuntadores por fila:
            tmp = self.primero  
            iFila = 1
            while tmp != None:
                if tmp.fila == iFila and tmp.columna < maxColumnas:
                    dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'->'+'columna'+str(tmp.fila)+str(tmp.columna+1)+';\n')
                else:
                    iFila += 1
                
                tmp = tmp.siguiente
                
            #Apuntadores para la primera columna:
            tmp = self.primero
            iColumna = 1
            while tmp is not None:
                if tmp.columna == iColumna and tmp.fila < maxFilas:
                    dot.write('columna'+str(tmp.fila)+str(tmp.columna)+'->'+'columna'+str(tmp.fila+1)+str(tmp.columna)+';\n')
                else:
                    pass
                tmp = tmp.siguiente


            dot.write('}\n')
            dot.write('}')

        system("dot -Tpng graphviz.dot -o patronFinal.png")
        startfile("patronFinal.png")
        
        
        

    