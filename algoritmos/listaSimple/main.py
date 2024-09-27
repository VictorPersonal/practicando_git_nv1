from lista import Lista

class Main():
    def main():
        opcion= 999
        
        miLista = Lista()
        while opcion != 0:
            dato= 0
            opcion = int(input("Menú Lista Simple:\n"+
                               "1. Agregar al inicio.\n"+
                               "2. Agregar al final\n"+
                               "3. Agregar Antes de \n"+
                               "4.Agregar Después de \n"+
                               "5. Eliminar al inicio \n"+
                               "6. Eliminar al final\n"+
                               "7. Eliminar antés de\n"+
                               "8. Eliminar después de\n"+
                               "9. Imprimir lista\n"+
                               "0. Salir\n"+
                               "Ingrese la opción -- >"))
            if opcion == 1:
                dato=int(input("Ingrese un dato para la lista: "))
                miLista.agregarInicio(dato)

            elif opcion == 2:
                dato=int(input("Ingrese un dato para la lista: "))
                miLista.agregarFinal(dato)


            elif opcion == 3:
                miLista.imprimirLista()
                criterio=int(input("Ingrese el criterio:s "))
                dato=int(input("Ingrese un dato para la lista: "))
                miLista.agregarAntes(dato,criterio)


            elif opcion == 4:
                miLista.imprimirLista()
                
                if miLista.getCabeza() != None:
                    criterio=int(input("Ingrese el criterio:s "))
                    dato=int(input("Ingrese un dato para la lista: "))
                    miLista.agregarDespues(dato,criterio)


            elif opcion == 5:
                miLista.eliminarInicio()

            elif opcion == 6:
                miLista.eliminarFinal()

            elif opcion == 7:
                miLista.imprimirLista()
                criterio=int(input("Ingrese el criterio de eliminación antes de: "))
                miLista.eliminarAntes(criterio)


            elif opcion == 8:
                miLista.imprimirLista()
                criterio=int(input("Ingrese el criterio de eliminación despues de: "))
                miLista.eliminarDespues(criterio)
            
            elif opcion == 9:
                miLista.imprimirLista()
            elif opcion == 0:
                print("Saliendo...")

            else:
                print("Opcion no valida")
    main()