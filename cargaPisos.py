from curses.ascii import ETB
from xml.dom import minidom
import xml.etree.ElementTree as ET
from listaPisos import listaPisos

class cargarPisos:
    def __init__(self):
        pass

    def MiniDom(ruta):
        mydoc = minidom.parse(ruta)
        piso = mydoc.getElementsByTagName('piso')
        print(piso)

    def elementTree(ruta):
        tree = ET.parse(ruta)
        raiz = tree.getroot()
        print(raiz)