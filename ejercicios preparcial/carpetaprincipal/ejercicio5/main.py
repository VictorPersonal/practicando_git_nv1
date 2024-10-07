from lista import Lista
class Main():
    def main():
        opcion= 999
        
        miLista = Lista()
        while opcion != 0:

            opcion = int(input("Menú Lista Simple:\n"+
                               "1. Agregar al final.\n"+
                               "2. Eliminar al final.\n"+
                               "Ingrese la opción --> "))
            
            if opcion == 1:
                for i in range(10):
                    dato=int(input(f"Ingrese el dato #{i+1}: "))
                    miLista.agregarFinal(dato)


                print("Lista original:")
                miLista.imprimirLista()

            elif opcion == 2:
                    miLista.eliminarFinal()
                    miLista.imprimirLista()
            



    main()