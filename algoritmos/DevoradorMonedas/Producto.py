class Producto():
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self.__precio = precio

    def impimirProducto(self):
        print(f"- {self.__codigo} {self.__nombre}: ${self.__precio}")