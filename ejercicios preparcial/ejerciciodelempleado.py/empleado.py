class Empleado():
    def __init__(self, nombre, cedula, edad, salario):
        self.nombre=nombre
        self.__cedula=cedula
        self.edad=edad
        self.__salario=salario
        
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario=salario

    def getCedula(self):
        return self.__cedula
    
    def setCedula(self, cedula):
        self.__cedula=cedula
