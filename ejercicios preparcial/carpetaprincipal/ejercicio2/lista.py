
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

    def eliminarInicio(self):

        # Comprobamos si la cabeza de la lista no es None (es decir, si la lista no está vacía).
        if self.__cabeza is not None:
            # Comprobamos si la cabeza y la cola son el mismo nodo, lo que significa que solo hay un nodo en la lista.
            if self.__cabeza == self.__cola:
                # Si solo hay un nodo, hacemos que tanto la cabeza como la cola apunten a None, vaciando la lista.
                self.__cabeza = None
                self.__cola = None
                print("Elemento eliminado exitosamente, la lista está vacía.")
            else:
                # Guardamos el nodo actual (que es la cabeza) en una variable temporal.
                nodoActual = self.__cabeza  
                
                # Actualizamos la cabeza de la lista para que apunte al siguiente nodo.
                self.__cabeza = self.__cabeza.getSig()  
                
                # Imprimimos un mensaje confirmando que el nodo actual (cabeza) ha sido eliminado.
                print(f"Elemento {nodoActual.getDato()} eliminado con éxito al inicio de la lista")
                
                # Eliminamos la referencia del nodo actual para ayudar al recolector de basura a liberar memoria.
                nodoActual.setSig(None)  

        else:
            # Si la cabeza es None, significa que la lista está vacía y no se puede eliminar nada.
            print("No se puede eliminar el elemento, la lista está vacía.")

    def imprimirLista(self):

        if self.__cabeza is not None:  # Verifica si la lista no está vacía.
            texto = ""  # Variable para almacenar los datos de los nodos en forma de cadena.
            nodoActual = self.__cabeza  # Comenzar desde el nodo cabeza.

            # Recorrer la lista hasta llegar al final (cuando nodoActual es None).
            while nodoActual is not None:
                texto += str(nodoActual.getDato()) + "->"  # Concatenar el dato del nodo actual.
                nodoActual = nodoActual.getSig()  # Avanzar al siguiente nodo.
            
            texto += "None"  # Agregar 'None' al final para representar el final de la lista.
            print("La lista actual es: " + texto)  # Imprimir la representación de la lista.

        else:
            # Si la lista está vacía, se notifica al usuario.
            print("La lista está vacía")

