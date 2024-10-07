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


    def eliminarFinal(self):
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:
                self.__cabeza=None
                self.__cola=None
            else:
                nodoActual=self.__cabeza
                while nodoActual.getSig() != self.__cola:
                    nodoActual = nodoActual.getSig()
                self.__cola = nodoActual
                nodoActual.setSig(None)
                print(f"Elemento {nodoActual.getDato()} eliminado con éxito al final de la lista")

        else:
            print("No se puede eliminar elementos, la lista está vacia.")

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
