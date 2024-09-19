
class Productos():
    def __init__(self, nombre, categoria,precioNeto, precioTotal,iva):
        self.nombre=nombre
        self.categoria=categoria
        self.precioN=precioNeto
        self.precioT=precioTotal
        self.iva=iva
    def calcularAcumPrecioTotalCatGranos(self,lista): #4n+4
        acumulado=0#1
        for producto in lista: #2n+2 --> 4n+2
            if producto.categoria == "granos": #1
                acumulado+=producto.precioT#1
            else:
                print("El producto no pertenece a la categoría granos")

        return acumulado #1

    def calcularAcumPrecioNetoCatLacteos(self,lista):#7n+4
        acumulado=0#1
        for producto in lista: #2n+2 --> 7n+2
            if (producto.categoria == "lacteos") and (producto.precioN > 13000): #3n
                acumulado+=producto.precioN#1n
                return acumulado#1n
            elif (producto.categoria != "lacteos") and (producto.precioN > 13000):#3
                print("El precio neto no puede ser acumulado")#1

            else:
                print("El precio neto no puede ser acumulado")
            
        return acumulado#1


    def calcularPromedioPrecioNetoCatVerduras(self, lista):#7n+4
        acum=0#1
        for producto in lista:#2n+2 --> 7n+2
            if (producto.categoria == "verduras"): #1n
                acum+=producto.precioN#1n
            promedio=acum/len(lista)#3n
        else:
            print("la categoría del producto es diferente a la de verdura")
        return promedio#1
    
    def calcularPromedioPrecioTotalCatAseo(self,lista):#8n+4
        acum=0#1
        for producto in lista:#2n+2-->8n+2
            if (producto.categoria == "aseo") and (producto.precioT < 20000):#3n
                acum+=producto.precioT#1n
                promedio=acum/len(lista)#3n
            elif (producto.categoria != "aseo") and (producto.precioT > 20000):
                print("El precio total no puede ser promediado")
            
            else:
                print("El precio total no puede ser promediado")

        return promedio#1
                
