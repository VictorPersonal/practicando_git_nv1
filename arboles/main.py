from ArbolBinario import ArbolBinario

class Main():
    def main():
        opcion=999
        arbolGenerado=ArbolBinario()
        while (opcion != 0):
            opcion=int(input("\nMENÚ\n1. Agregar Nodo.\n2. Recorrer inorden.\n3. Recorrer preorden\n4. Recorrer postorden.\n5. Buscar nodo\n6. Eliminar nodo\n0. Salir\n->"))
            if(opcion==1):
                dato=int(input("Ingrese el dato del nuevo nodo: "))
                arbolGenerado.insertarNodo(dato, arbolGenerado.getRaiz())
            elif(opcion==2):
                arbolGenerado.recorrerInOrden(arbolGenerado.getRaiz())
            elif(opcion==3):
                arbolGenerado.recorrerPreorden(arbolGenerado.getRaiz())
            elif(opcion==4):
                arbolGenerado.recorrerPostOrden(arbolGenerado.getRaiz())
            elif(opcion==5):
                dato=int(input("Ingrese el dato a buscar: "))
                arbolGenerado.buscarNodo(dato,arbolGenerado.getRaiz())
            elif(opcion==6):
                dato=int(input("Ingrese el dato a eliminar: "))
                arbolGenerado.eliminarNodo(dato, arbolGenerado.getRaiz())
            elif(opcion==0):
                print("Saliendo del sistema")
            else:
                print("Opción no valida")
    main()
