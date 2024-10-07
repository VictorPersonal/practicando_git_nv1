class Nodo():
    def __init__(self, dato):
        self.__dato=dato
        self.__sig=None

    def getDato(self):
        return self.__dato
    def setDato(self,dato):
        self.__dato=dato
    def getSig(self):
        return self.__sig
    def setSig(self, sig):
        self.__sig=sig