from nodo import Nodo

class AgregarInicio:
    def __init__(self, lista):
        self.lista = lista

    def AgregarInicioLista(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.setSiguiente(self.lista.getCabeza())
        self.lista.setCabeza(nuevo_nodo)
