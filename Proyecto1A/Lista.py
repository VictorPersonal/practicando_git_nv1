__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

class Lista():
    """Esta clase representa la lista en donde van a ser almacenados los nodos.
        Attributes:
            cabeza(any)=[cabeza]
    """
    def __init__(self):#1
        """Este método nos permite crear objetos o instancias que simula una lista o "cola", esto interactua como base del sistema.
            Args:
                param1: cabeza(any)=[None]
        """
        self.cabeza = None #1

    def getCabeza(self): #1
        """Este método nos permite saber cual es la cabeza o primer nodo de una lista en concreto.
            Args:
            Returns:
                cabeza(any)
        """
        return self.cabeza #1
    
    def setCabeza(self, cabeza): #1
        """Este método nos permite modificar la cabeza o primer nodo de una lista en concreto.
            Args:
                param1: cabeza(any)=[cabeza]
        """
        self.cabeza = cabeza #1

    def imprimirLista(self):#5n+10
        """Este método nos permite imprimir (o no, si la lista está vacía) cada nodo de la lista empezando por la cabeza.
            Args:
            Returns:
        """
        nodo_actual = self.cabeza#1
        if nodo_actual is None:#1
            print("La lista está vacía.")#1
            return #1
        while nodo_actual is not None:#n+1 --> 5n+5 
            print(f"{nodo_actual.getDato()}", end=" -> \n")#2(n+1) --> 2n+2
            nodo_actual = nodo_actual.getSiguiente()#2(n+1) --> 2n+2
            
        print("None")#1