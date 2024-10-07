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
            print(f"Dato {dato} agregado al final de la lista con éxito")

    def eliminarDespuesDeMayorQue21(self):

        nodoActual = self.__cabeza  
        while nodoActual is not None:  
            if nodoActual.getDato() > 21:  
                nodoAEliminar = nodoActual.getSig()  
                if nodoAEliminar is not None:  
                    nodoActual.setSig(nodoAEliminar.getSig())  
                    if nodoAEliminar == self.__cola:
                        self.__cola = nodoActual  
                    print(f"Elemento {nodoAEliminar.getDato()} eliminado con éxito.")
                    return
                else:
                    print("No hay un nodo para eliminar después del nodo mayor a 21.")
                    return
            nodoActual = nodoActual.getSig()  
        print("No se encontró un nodo mayor a 21.")  

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
