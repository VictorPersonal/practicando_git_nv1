from nodo import Nodo

class Lista:
    
    def __init__(self):

        self.__cabeza = None
        self.__cola = None

    def getCabeza(self):

        return self.__cabeza

    def setCabeza(self, cabeza):

        self.__cabeza = cabeza

    def getCola(self):

        return self.__cola

    def setCola(self, cola):

        self.__cola = cola

    def validarListaVacia(self, dato):
        if self.__cabeza is None and self.__cola is None:
            # Si la cabeza y la cola son None, la lista está vacía.
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo con el dato.
            self.__cabeza = nuevoNodo  # Asignar el nuevo nodo como cabeza.
            self.__cola = nuevoNodo  # Asignar el nuevo nodo como cola.
            print(f"Primer Dato {dato} agregado a la lista con éxito")
            return True
        return False
    
    def agregarFinal(self, dato):
        if self.validarListaVacia(dato):
            pass

        else:
            nuevoNodo=Nodo(dato)
            self.__cola.setSig(nuevoNodo)
            self.__cola=nuevoNodo
            print(f"Dato {dato} agregado al final de la lista")


    def eliminarAntesDeMayorQue37(self, criterio=37):
        # Verificamos si la lista tiene al menos dos nodos
        if self.__cabeza is None or self.__cabeza.getSig() is None:
            print("No se puede eliminar, la lista tiene menos de dos nodos.")
            return

        # Caso especial: si el nodo a eliminar es el primero
        if self.__cabeza.getSig().getDato() > criterio:
            print(f"Elemento {self.__cabeza.getDato()} eliminado con éxito (nodo cabeza).")
            self.__cabeza = self.__cabeza.getSig()  # El nuevo cabeza será el siguiente nodo
            return

        # Recorremos la lista buscando el nodo cuyo siguiente tiene un valor mayor a 37
        nodoActual = self.__cabeza

        while nodoActual.getSig() is not None:  # Recorremos mientras haya nodos por revisar
            siguienteNodo = nodoActual.getSig().getSig()  # Verificamos dos nodos adelante
            if siguienteNodo is not None and siguienteNodo.getDato() > criterio:
                # Si encontramos un nodo con valor mayor a 37
                print(f"Elemento {nodoActual.getSig().getDato()} eliminado con éxito.")
                nodoActual.setSig(siguienteNodo)  # Eliminamos el nodo intermedio
                return
            nodoActual = nodoActual.getSig()

        print("No se encontró ningún nodo con valor mayor a 37.")

            
        
    def imprimirLista(self):

        if self.__cabeza is not None:  
            texto = ""  
            nodoActual = self.__cabeza  

            # Recorrer la lista hasta llegar al final (cuando nodoActual es None)
            while nodoActual is not None:
                texto += str(nodoActual.getDato()) + " -> "  
                nodoActual = nodoActual.getSig()  
            
            texto += "None"  
            print("La lista actual es: " + texto)  

        else:
            
            print("La lista está vacía")
