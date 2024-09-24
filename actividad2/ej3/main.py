from votantes import Votante

class Main():
    def main():
        gestor=Votante()
        opcion=999
        print("Seleccione la opción:\n1. Crear votantes.\n2. Seleccionar Votantes.\n3.Mostrar resultados.")
        print("Ingrese su opción: ")
        if opcion == 1:
            Votante.ingresarAlVotante()
    
    main()