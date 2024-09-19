from ejercicio1 import Productos
class Main():
    def main():#20n+3
        listaProductos=[]#1
        
        for producto in range(12):#2n+2--> 20n+2
            print(f"Producto ingresado número {producto+1}")#2
            n=input("Ingrese el nombre del producto: ")#1
            c=input("Ingrese la categoria del producto: ").lower()#2
            pn=int(input("Ingrese el precio neto: "))#2
            pt=int(input("Ingrese el precio total: "))#2
            iva=float(input("Ingrese el iva: "))#2
            productoGuardado=Productos(n,c,pn,pt,iva)#6
            listaProductos.append(productoGuardado)#1
            print("Guardado :)""\n")#1
        productoGuardado.calcularAcumPrecioNetoCatLacteos(listaProductos)#7n+4
        productoGuardado.calcularAcumPrecioTotalCatGranos(listaProductos)#4n+4
        productoGuardado.calcularPromedioPrecioNetoCatVerduras(listaProductos)#7n+4
        productoGuardado.calcularPromedioPrecioTotalCatAseo(listaProductos)#8n+4
    
    main()#46n+10