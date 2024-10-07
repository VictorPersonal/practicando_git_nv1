from nodo import Nodo

class Lista():

    def __init__(self):
        self.__cabeza=None
        self.__cola=None

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
            print(f"Dato {dato} agregado con éxito al final de la lista")


    def eliminarNodoEntrePosiciones(self, inicio):
        """
        Elimina el nodo que se encuentra justo después del nodo en la posición 'inicio'.
        :param inicio: Posición inicial del nodo anterior al que se eliminará.
        """
        nodoActual = self.__cabeza
        index = 0

        # Recorrer hasta llegar a la posición de inicio
        while nodoActual is not None and index < inicio:
            nodoAnterior = nodoActual  # Guardamos el nodo anterior
            nodoActual = nodoActual.getSig()
            index += 1

        # Si estamos en la posición de inicio, continuamos buscando el nodo a eliminar
        if nodoActual is not None:
            nodoAEliminar = nodoActual.getSig()  # Nodo a eliminar es el siguiente al nodoActual

            if nodoAEliminar is not None:
                # Actualizamos la referencia del nodo anterior
                nodoAnterior.setSig(nodoAEliminar.getSig())
                if nodoAEliminar == self.__cola:
                    self.__cola = nodoAnterior  # Actualizar la cola si eliminamos el último nodo
                print(f"Elemento {nodoAEliminar.getDato()} eliminado con éxito.")
            else:
                print("No hay un nodo para eliminar después del nodo en la posición especificada.")
        else:
            print("No se encontró un nodo en la posición especificada.")


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
