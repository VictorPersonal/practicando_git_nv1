class Nodo():
    def __init__(self, dato):
        self.__padre=None
        self.__dato=dato
        self.__izquierda=None
        self.__derecho=None


    def getDato(self):
        return self.__dato
    
    def setDato(self,dato):
        self.__dato=dato

    def getPadre(self):
        return self.__padre
    
    def setPadre(self, padre):
        self.__padre=padre

    def getIzq(self):
        return self.__izquierda
    
    def setIzq(self,izq):
        self.__izquierda=izq

    def getDer(self):
        return self.__derecho
    
    def setDer(self,der):
        self.__derecho=der