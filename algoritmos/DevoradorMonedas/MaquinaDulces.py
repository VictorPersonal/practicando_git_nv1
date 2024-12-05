from Producto import Producto
from Moneda import Moneda

class MaquinaDulces():
    def __init__(self, proveedor):
        self.__proveedor = proveedor
        self.__productos = []
        self.__monedas1000 = []
        self.__monedas500 = []
        self.__monedas200 = []
        self.__monedas100 = []
        self.__monedas50 = []

    def getProveedor(self):
        return self.__proveedor    
    def getProductos(self):
        return self.__productos
    def getMonedas1000(self):
        return self.__monedas1000
    def getMonedas500(self):
        return self.__monedas500
    def getMonedas200(self):
        return self.__monedas200
    def getMonedas100(self):
        return self.__monedas100
    def getMonedas50(self):
        return self.__monedas50
    
    def setProveedor(self, proveedor):
        self.__proveedor = proveedor
    def setProductos(self, productos):
        self.__productos = productos
    def setMonedas1000(self, monedas1000):
        self.__monedas1000 = monedas1000
    def setMonedas500(self, monedas500):
        self.__monedas500 = monedas500
    def setMonedas200(self, monedas200):
        self.__monedas200 = monedas200
    def setMonedas100(self, monedas100):
        self.__monedas100 = monedas100
    def setMonedas50(self, monedas50):
        self.__monedas50 = monedas50

    def agregarProductos(self):
        codigo = len(self.__productos)
        nombre = input("Ingrese el nombre del nuevo Producto: ")
        precio = int(input("Ingrese el precio del nuevo Producto: "))
        miProducto = Producto(codigo, nombre, precio)
        self.__productos.append(miProducto)

    def cargarMonedas(self):
        for _ in range(10):
            self.__monedas1000.append(Moneda(1000))
        for _ in range(20):
            self.__monedas500.append(Moneda(500))
        for _ in range(30):
            self.__monedas200.append(Moneda(200))
        for _ in range(40):
            self.__monedas100.append(Moneda(100))
        for _ in range(50):
            self.__monedas50.append(Moneda(50))