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

    def agregarInicio(self, dato):

        if self.validarListaVacia(dato):
            # Si la lista estaba vacía, el método anterior ya agregó el primer nodo.
            pass
        else:
            # Crear un nuevo nodo y hacerlo la nueva cabeza.
            nuevoNodo = Nodo(dato)
            nuevoNodo.setSig(self.__cabeza)  # El nuevo nodo apunta a la antigua cabeza.
            self.__cabeza = nuevoNodo  # Actualizar la cabeza.
            print(f"Dato {dato} agregado al inicio de la lista con éxito")


    def imprimirLista(self):
        """
        Imprime los elementos de la lista enlazada desde la cabeza hasta el último nodo.
        Muestra los valores conectados por '->' y al final indica que no hay más nodos con 'None'.
        """
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