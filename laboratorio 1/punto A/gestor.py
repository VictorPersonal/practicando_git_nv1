
#Cuando se borra el primer registro sale un none, junto con el resto de elementos

import random
class Beneficiario():
    def __init__(self, nombre,edad,subsidio=0):
        self.nombre=nombre
        self.__edad=edad
        self.__subsidio=subsidio

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad=edad

    def getSubsidio(self):
        return self.__subsidio
    
    def setSubsidio(self, subsidio):
        self.__subsidio=subsidio
    
    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.getEdad()}, Valor Subsidio: {self.getSubsidio()}"
    
    def agregarBeneficiario(self, lista):#Esta incompleto,ps le falta aclarar lo del subsidio
        for i in range(5):
            nombre=input("Ingrese el nombre: ")
            edad=random.randint(5,17)
            print(f"Edad del benficiario es: {edad}")
            subsidio=self.getSubsidio()
            personaAgregada=Beneficiario(nombre,edad,subsidio)
            lista.append(personaAgregada)
        
    
    def mostrarBeneficiario(self,lista):
        for persona in lista:
            print(persona)

    def pagarBeneficiario(self, beneficiario):
        pago1=60000
        pago2=80000
        pago3=100000
            
        if beneficiario.getEdad() >= 5 and beneficiario.getEdad() <= 9:
            beneficiario.setSubsidio(beneficiario.getSubsidio() + pago1)
        elif beneficiario.getEdad() > 9 and beneficiario.getEdad() <= 13:
            beneficiario.setSubsidio(beneficiario.getSubsidio() + pago2)
        elif beneficiario.getEdad() > 13 and beneficiario.getEdad() <= 17:
            beneficiario.setSubsidio(beneficiario.getSubsidio() + pago3)
        else:
            print("La edad que marcó no está dentro de los rangos permitidos")


    def pagarYSacarBen(self, lista):
        while lista:
            
            # Pagar subsidio al primer beneficiario y mostrarlo
            print("\nPagando subsidio al primer beneficiario en la lista:")
            self.pagarBeneficiario(lista[0])
            print(lista[0])

            # Eliminar el primer beneficiario de la lista después de pagar
            lista.pop(0)
            print("\nPrimer beneficiario eliminado de la lista.")

            # Mostrar el resto de beneficiarios sin subsidio
            print("\nBeneficiarios restantes sin subsidio:")
            self.mostrarBeneficiario(lista)
            


listaPaAgregar=[]
persona=Beneficiario("none",21)
persona.agregarBeneficiario(listaPaAgregar)
#persona.sacarBeneficiario(listaPaAgregar)
persona.pagarYSacarBen(listaPaAgregar)




        