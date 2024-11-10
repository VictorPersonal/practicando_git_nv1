__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

class Nodo():
    """Esta clase representa el o los nodos que van a pertenecer a la lista.
        Attributes:
            dato(any)=[dato]
            siguiente(reference)=[siguiente]
    """
    def __init__(self, dato):#2
        """Este método crea objetos o instancias de la clase Nodo, que interactuan con la clase Lista.
            Args:
                param1: dato(any)=[dato]
                param2: siguiente(reference)=[None]
        """
        self.dato = dato#1
        self.siguiente = None#1

    def getDato(self):#1
        """Este método retorna el dato del nodo consultado.
            Args:
            Returns:
                dato(any)
        """
        return self.dato #1
    
    def getSiguiente(self):#1
        """Este método retorna el puntero o refencia de un nodo consultado.
            Args:
            Returns:
                siguiente(reference)
        """
        return self.siguiente #1
    
    def setDato(self, dato):#1
        """Este método modifica el dato que hay en un nodo en concreto.
            Args:
                param1: dato(any)=[dato]
        """
        self.dato = dato#1

    def setSiguiente(self, siguiente):#1
        """Este método modifica el puntero o referencia de un nodo en concreto.
            Args:
                param1: siguiente(reference)=[siguiente]
        """
        self.siguiente = siguiente#1
