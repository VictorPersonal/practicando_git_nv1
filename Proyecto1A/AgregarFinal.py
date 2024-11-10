__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

from Nodo import Nodo
import sys
class AgregarFinal():
    """Esta clase representa una acción la cual sirve para agregar un nodo a una lista en concreto.
        Attributes:
            lista(list)=[lista]
    """
    def __init__(self, lista):#1
        """Este método nos permite crear objetos o instancias de la clase AgregarFinal, la cual interactua en el Main con las personas.
            Args:
                param1: lista(list)=[lista]
        """
        self.lista = lista #1
    """
    def agregarFinalLista(self, dato):#3n+8
        
        nuevo_nodo = Nodo(dato)#2

        # Si la lista está vacía, el nuevo nodo será la cabeza
        if self.lista.getCabeza() is None:#1
            self.lista.setCabeza(nuevo_nodo)#1
        else:

            # Recorre la lista hasta el último nodo
            nodo_actual = self.lista.getCabeza()#2
            #3n+1
        
            while nodo_actual.getSiguiente() is not None:#n+1           n veces desde el inicio del bucle hasta la vez que se rompe el bucle, por lo que se suma 1.
                nodo_actual = nodo_actual.getSiguiente()#2*n            2 por lo que consume la linea 
                
            # Agrega el nuevo nodo al final
            nodo_actual.setSiguiente(nuevo_nodo)#1
    """


    def calcularPesoCompleto(self):
        """Calcula el peso de la lista incluyendo todos los nodos."""
        peso_total = sys.getsizeof(self.lista)  # Tamaño base de la lista
        nodo_actual = self.lista.getCabeza()

        while nodo_actual is not None:
            peso_total += sys.getsizeof(nodo_actual)  # Agrega el tamaño del nodo
            nodo_actual = nodo_actual.getSiguiente()  # Avanza al siguiente nodo

        return peso_total
    def agregarFinalLista(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.lista.getCabeza() is None:
            self.lista.setCabeza(nuevo_nodo)
        else:
            nodo_actual = self.lista.getCabeza()
            count = 1
            while nodo_actual.getSiguiente() is not None:
                nodo_actual = nodo_actual.getSiguiente()
                count += 1

            nodo_actual.setSiguiente(nuevo_nodo)
            count += 1

            if count == 50:
                peso_completo = self.calcularPesoCompleto()
                print(f"El peso completo de la lista con 50 elementos es de: {peso_completo} bytes")
