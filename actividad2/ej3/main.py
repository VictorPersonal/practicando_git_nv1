from votantes import Votante

class Main():
    def main():
        miVotante=Votante("andres",12,"M")
        opcion=999
        while opcion != 0:
            print()
            opcion=int(input("Seleccione la opción:\n1. Crear votantes.\n2 .Mostrar resultados.\nIngrese su opción: "))
            if opcion == 1:
                miVotante.ingresarAlVotante()
            elif opcion == 2:
                miVotante.mostrarResult()
            else:
                print("Opcion no valida")
        
    main()