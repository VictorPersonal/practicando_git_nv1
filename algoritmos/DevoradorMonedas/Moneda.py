class Moneda():
    def __init__(self, denominacion):
        self.__denominacion = denominacion

    def getDenominacion(self):
        return self.__denominacion
    
    def setDenominacion(self, denominacion):
        self.__denominacion = denominacion