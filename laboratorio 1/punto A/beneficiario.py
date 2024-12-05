
from lista import Lista

import random
import random
contadorDinero=0
contadorPersonas=0
class Beneficiario():
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.__edad=edad
        #self.__subsidio=subsidio

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad=edad


    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.getEdad()}"
    
    
    def agregarBeneficiario(self,listaA):
        nombres=["Alexa","María","Brandon","Valentina","Víctor","Sofía","Lucas","Juan","Marcela","Nicolas"]
        for _ in range(50):
            nombre=random.choice(nombres)
            edades=random.randint(5,17)
            personaAgregada=Beneficiario(nombre, edades)
            #Agregar funcion de la lista.
            listaA.agregarFinal(personaAgregada)

    #AGREGAR METODO PARA PAGAR SUBSIDIO TENIENDO EN CUENTA EL METODO DE ELIMINAR INICIO DE LISTA

    def calcularMonto(self,edad):
        try:
            if  5<= edad <=9:
                return 6000
            
            elif 10<= edad <=13:
                return 8000

            elif 14 <= edad <= 17:
                return 10000
            else:
                print(f"La edad de {edad} años no está permitida")
        except TypeError as er:
            print(f"El tipo de dato es erroneo {er}")

    def sacarBeneficiario(self, lista):
        global  contadorDinero
        global contadorPersonas
        # Obtener el primer beneficiario de la lista
        beneficiario = lista.getCabeza().getDato()

        # Calcular el subsidio basado en la edad del beneficiario
        subsidio = self.calcularMonto(beneficiario.getEdad())
        
        if subsidio:
            contadorDinero+=subsidio
            contadorPersonas+=1
            print(f"Subsidio de {subsidio} reclamado por {beneficiario.nombre}")
            lista.eliminarInicio()  # Elimina al primer beneficiario después de "entregar el subsidio"

    def contarPersonas(self):
        global contadorPersonas
        print(f"La cantidad de personas que han retirado el subsidio es de {contadorPersonas} personas.")

    def contarDinero(self):
        global contadorDinero
        print(f"El total de dinero entregado en subsidios es de {contadorDinero} pesos.")

