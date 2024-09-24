from ejercicio1 import Productos
class Main():
    def main():#26n+2+1=26n+3
        listaProductos=[]#1
        
        for producto in range(12):#2n+2--> 26n+2
            print(f"Producto ingresado número {producto+1}")#2n
            n=input("Ingrese el nombre del producto: ")#2n
            c=input("Ingrese la categoria del producto: ").lower()#3n
            pn=int(input("Ingrese el precio neto: "))#3n
            pt=int(input("Ingrese el precio total: "))#3n
            iva=float(input("Ingrese el iva: "))#3n
            productoGuardado=Productos(n,c,pn,pt,iva)#6n
            listaProductos.append(productoGuardado)#1n
            print("Guardado :)""\n")#1n
        productoGuardado.calcularAcumPrecioNetoCatLacteos(listaProductos)#7n+4
        productoGuardado.calcularAcumPrecioTotalCatGranos(listaProductos)#4n+4
        productoGuardado.calcularPromedioPrecioNetoCatVerduras(listaProductos)#7n+4
        productoGuardado.calcularPromedioPrecioTotalCatAseo(listaProductos)#8n+4
    
    main()
#O(n)=52n+19