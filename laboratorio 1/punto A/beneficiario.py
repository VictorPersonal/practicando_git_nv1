
from lista import Lista

import random
import random
class Beneficiario():
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.__edad=edad
        #self.__subsidio=subsidio

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad=edad

    """def getSubsidio(self):
        return self.__subsidio
    """
    """def setSubsidio(self, subsidio):
        self.__subsidio=subsidio
    """
    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.getEdad()}"
    

    

    
    def agregarBeneficiario(self,listaA):
        nombres=["Alexa","María","Brandon","Valentina","Víctor","Sofía","Lucas","Juan","Marcela","Nicolas"]
        for _ in range(5):
            nombre=random.choice(nombres)
            edades=random.randint(5,17)
            personaAgregada=Beneficiario(nombre, edades)
            #Agregar funcion de la lista.
            listaA.agregarFinal(personaAgregada)

    #AGREGAR METODO PARA PAGAR SUBSIDIO TENIENDO EN CUENTA EL METODO DE ELIMINAR INICIO DE LISTA

            

miLista=Lista()

persona=Beneficiario("julia",12)
persona.agregarBeneficiario(miLista)
print("Lista Beneficiarios:")
miLista.mostrarLista()
