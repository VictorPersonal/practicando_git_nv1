
from filesistem import FileSystem
class Main():
    def main():
        fs=FileSystem()
        opcion=999
        while (opcion!=0):
            opcion=int(input("\nMenú Principal\n"
                             "1. Crear un archivo/carpeta\n"
                             "2. Listar el directorio actual\n"
                             "3. Cambiar directorio\n"
                             "4. Eliminar archivo/carpeta\n"
                             "5. Buscar archivo/carpeta\n"
                             "6. Salir\n"
                             "--> "))
            

            if (opcion == 1):
                nombre = input("Ingrese el nombre del archivo o carpeta: ").lower()
                tipo = input("¿Es un archivo o carpeta? (archivo/carpeta): ").lower()
                fs.crearEnConsola(nombre,tipo)


            elif (opcion == 2):
                fs.listarEnConsola()

            elif (opcion == 3):
                nombre = input("Ingrese el nombre del directorio al que desea acceder o '..' para volver al padre: ").lower()
                fs.cambiar_directorio(nombre)

            elif (opcion == 4):
                nombre = input("Ingrese el nombre del archivo o carpeta a eliminar: ")
                fs.eliminar(nombre)
            

            elif (opcion == 5):
                nombre = input("Ingrese el nombre del archivo o carpeta a buscar: ")
                fs.buscarEnConsola(nombre)

            
            elif (opcion == 6):
                break

            else:
                print("Opción no válida. Intente de nuevo.")


    main()


        
        
            

        
        
            
        
        
