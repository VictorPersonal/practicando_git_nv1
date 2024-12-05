

"""[[1000 1000 1000]
 [500 500 500]
 [200 200 200]]"""

class Devorador():
    def __init__(self):
        self.__candidatos = []
        self.__solucion = []
        self.__rechazados = []

    def getSolucion(self):
        return self.__solucion
    def getCandidatos(self):
        return self.__candidatos
    def getRechazados(self):
        return self.__rechazados
    
    def setSolucion(self, solucion):
        self.__solucion = solucion
    def setCandidatos(self, candidatos):
        self.__candidatos = candidatos
    def setRechazados(self, rechazados):
        self.__rechazados = rechazados

    def validarSolucion(self, cambio):
        if(cambio == 0):
            return True
        else:
            return False

    def seleccionarCandidato(self, cambio):
        if(self.__candidatos[0][0].getDenominacion() <= cambio and len(self.__candidatos[0]) > 0):
            candidato = self.__candidatos[0][0]
            self.__candidatos[0].pop(0)
            return candidato
        elif(self.__candidatos[1][0].getDenominacion() <= cambio and len(self.__candidatos[1]) > 0):
            candidato = self.__candidatos[1][0]
            self.__candidatos[1].pop(0)
            return candidato
        elif(self.__candidatos[2][0].getDenominacion() <= cambio and len(self.__candidatos[2]) > 0):
            candidato = self.__candidatos[2][0]
            self.__candidatos[2].pop(0)
            return candidato
        elif(self.__candidatos[3][0].getDenominacion() <= cambio and len(self.__candidatos[3]) > 0):
            candidato = self.__candidatos[3][0]
            self.__candidatos[3].pop(0)
            return candidato
        elif(self.__candidatos[4][0].getDenominacion() <= cambio and len(self.__candidatos[4]) > 0):
            candidato = self.__candidatos[4][0]
            self.__candidatos[4].pop(0)
            return candidato
        else:
            return None
        
    def insertarCandidato(self, candidato, cambio):
        self.__solucion.append(candidato)
        cambio -= candidato.getDenominacion()
        return cambio

    def validarListasVacias(self):
        if(len(self.__candidatos[0]) == 0 and len(self.__candidatos[1]) == 0 and len(self.__candidatos[2]) == 0 and len(self.__candidatos[3]) == 0 and len(self.__candidatos[4]) == 0):
            return True
        else:
            return False

    def buscarSolucion(self, cambio):
        while(not self.validarListasVacias() and not self.validarSolucion(cambio)):
            candidato = self.seleccionarCandidato(cambio)
            if(candidato != None):
                cambio = self.insertarCandidato(candidato, cambio)
            else:
                print("La maquina no posee monedas suficientes para dar su devuelta...")
        if(not self.validarSolucion(cambio)):
            print("Ha sucedido un error, por favor pongase en contacto con el proveedor...")
        else:
            for moneda in self.__solucion:
                print(moneda.getDenominacion())