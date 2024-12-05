from MaquinaDulces import MaquinaDulces
from Devorador import Devorador

class Main():
    def main():
        miMaquina = MaquinaDulces("Nova Venta")
        miMaquina.cargarMonedas()

        miDevorador = Devorador()
        listaCandidatos = miDevorador.getCandidatos()
        listaCandidatos.append(miMaquina.getMonedas1000())
        listaCandidatos.append(miMaquina.getMonedas500())
        listaCandidatos.append(miMaquina.getMonedas200())
        listaCandidatos.append(miMaquina.getMonedas100())
        listaCandidatos.append(miMaquina.getMonedas50())
        miDevorador.setCandidatos(listaCandidatos)

        for _ in range(4):
            miMaquina.agregarProductos()

        listaProductos = miMaquina.getProductos()
        for producto in listaProductos:
            producto.impimirProducto()

        pago = int(input("Ingrese el dinero: "))

        compra = int(input("Ingrese el código del producto a comprar: "))

        precio = 0

        for producto in listaProductos:
            if(producto.getCodigo() == compra):
                precio = producto.getPrecio()
                break
        
        cambio = pago-precio

        if(cambio > 0):
            miDevorador.buscarSolucion(cambio)
        else:
            print("El dinero ingresado no es suficiente para comprar el producto seleccionado...")


    main()