import random
class Beneficiario():
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.__edad=edad

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad=edad
    
    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.getEdad()}"
    
    def agregarBeneficiario(self, lista):
        for i in range(5):
            nombre=input("Ingrese el nombre: ")
            edad=random.randint(0,10)
            print(f"Edad del benficiario es: {edad}")
            personaAgregada=Beneficiario(nombre,edad)
            lista.append(personaAgregada)
        
    
    def mostrarBeneficiario(self,lista):
        for persona in lista:
            print(persona)

    def sacarBeneficiario(self,lista):
        for beneficiario in lista:
            
            if beneficiario.getEdad() ==5:
                print(f"Lista antes de: ")
                self.mostrarBeneficiario(lista)
                print("Beneficiario a eliminar es {}".format(beneficiario.nombre))
                lista.remove(beneficiario)
                #lista.pop(0)
                print(f"Lista antes de: ")
                self.mostrarBeneficiario(lista)
                break
            else:
                print("El beneficiario es mayor a 5 años")

listaPaAgregar=[]
persona=Beneficiario("none",21)
persona.agregarBeneficiario(listaPaAgregar)
persona.sacarBeneficiario(listaPaAgregar)




        