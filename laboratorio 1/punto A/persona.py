class Persona():
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad