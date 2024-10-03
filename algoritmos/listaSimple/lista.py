from nodo import Nodo

class Lista:
    """
    Clase que representa una lista enlazada.
    Gestiona nodos con punteros a los siguientes nodos, permitiendo
    operaciones como agregar, eliminar y verificar elementos.
    """
    
    def __init__(self):
        """
        Inicializa una lista vacía, donde la cabeza y la cola son None.
        """
        self.__cabeza = None
        self.__cola = None

    def getCabeza(self):
        """
        Obtiene el nodo cabeza de la lista.
        :return: Nodo que está al inicio de la lista.
        """
        return self.__cabeza

    def setCabeza(self, cabeza):
        """
        Establece el nodo cabeza de la lista.
        :param cabeza: Nodo a ser asignado como cabeza.
        """
        self.__cabeza = cabeza

    def getCola(self):
        """
        Obtiene el nodo cola de la lista.
        :return: Nodo que está al final de la lista.
        """
        return self.__cola

    def setCola(self, cola):
        """
        Establece el nodo cola de la lista.
        :param cola: Nodo a ser asignado como cola.
        """
        self.__cola = cola

    def validarListaVacia(self, dato):
        """
        Verifica si la lista está vacía. Si lo está, agrega el primer nodo.
        :param dato: Valor a almacenar en el nuevo nodo.
        :return: True si la lista estaba vacía y se agregó el primer nodo, False si no.
        """
        if self.__cabeza is None and self.__cola is None:
            # Si la cabeza y la cola son None, la lista está vacía.
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo con el dato.
            self.__cabeza = nuevoNodo  # Asignar el nuevo nodo como cabeza.
            self.__cola = nuevoNodo  # Asignar el nuevo nodo como cola.
            print(f"Primer Dato {dato} agregado a la lista con éxito")
            return True
        return False

    def agregarInicio(self, dato):
        """
        Agrega un nuevo nodo al inicio de la lista.
        :param dato: Valor a almacenar en el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            # Si la lista estaba vacía, el método anterior ya agregó el primer nodo.
            pass
        else:
            # Crear un nuevo nodo y hacerlo la nueva cabeza.
            nuevoNodo = Nodo(dato)
            nuevoNodo.setSig(self.__cabeza)  # El nuevo nodo apunta a la antigua cabeza.
            self.__cabeza = nuevoNodo  # Actualizar la cabeza.
            print(f"Dato {dato} agregado al inicio de la lista con éxito")

    def agregarFinal(self, dato):
        """
        Agrega un nuevo nodo al final de la lista.
        :param dato: Valor a almacenar en el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            pass
        else:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo.
            self.__cola.setSig(nuevoNodo)  # La cola actual apunta al nuevo nodo.
            self.__cola = nuevoNodo  # Actualizar la cola.
            print(f"Dato {dato} agregado al final de la lista con éxito")

    def agregarAntes(self, dato, criterio):
        """
        Agrega un nuevo nodo antes de un nodo que cumpla con el criterio dado.
        :param dato: Valor a almacenar en el nuevo nodo.
        :param criterio: Valor del nodo antes del cual se va a insertar el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            pass
        elif self.__cabeza.getDato() == criterio:
            # Si el criterio está en la cabeza, simplemente agregar al inicio.
            self.agregarInicio(dato)
        else:
            nuevoNodo = Nodo(dato)
            nodoActual = self.__cabeza  # Inicia desde la cabeza.
            # Busca el nodo antes del nodo que tiene el valor del criterio.
            while nodoActual.getSig().getDato() != criterio:
                if nodoActual.getSig() is not None:
                    nodoActual = nodoActual.getSig()
                else:
                    break
            # Insertar el nuevo nodo.
            nuevoNodo.setSig(nodoActual.getSig())
            nodoActual.setSig(nuevoNodo)
            print(f"Dato {dato} agregado a la lista antes de {criterio} con éxito")

    def agregarDespues(self, dato, criterio):
        """
        Agrega un nuevo nodo después de un nodo que cumpla con el criterio dado.
        :param dato: Valor a almacenar en el nuevo nodo.
        :param criterio: Valor del nodo después del cual se va a insertar el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            pass
        else:
            nuevoNodo = Nodo(dato)
            nodoActual = self.__cabeza
            # Busca el nodo que coincide con el criterio.
            while nodoActual.getDato() != criterio:
                if nodoActual.getSig() is not None:
                    nodoActual = nodoActual.getSig()
                else:
                    break
            # Insertar el nuevo nodo después del nodo encontrado.
            nuevoNodo.setSig(nodoActual.getSig())
            nodoActual.setSig(nuevoNodo)
            if nodoActual == self.__cola:
                self.__cola = nuevoNodo
            print(f"Dato {dato} agregado a la lista después de {criterio} con éxito")

    def eliminarInicio(self):
        """
        Elimina el nodo al inicio de la lista.
        """
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:
                # Si solo hay un nodo, la lista se vacía.
                self.__cabeza = None
                self.__cola = None
                print("Elemento eliminado exitosamente, la lista está vacía.")
            else:
                nodoActual = self.__cabeza  # Guardar la cabeza actual.
                self.__cabeza = self.__cabeza.getSig()  # Actualizar la cabeza.
                print(f"Elemento {nodoActual.getDato()} eliminado con éxito al inicio de la lista")
                nodoActual.setSig(None)  # Eliminar la referencia del nodo.

        else:
            print("No se puede eliminar el elemento, la lista está vacía.")

    def eliminarFinal(self):
        """
        Elimina el nodo al final de la lista.
        """
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:
                self.__cabeza = None
                self.__cola = None
            else:
                nodoActual = self.__cabeza
                # Buscar el penúltimo nodo.
                while nodoActual.getSig() != self.__cola:
                    nodoActual = nodoActual.getSig()
                self.__cola = nodoActual  # El penúltimo nodo se convierte en la nueva cola.
                nodoActual.setSig(None)  # Eliminar la referencia al antiguo último nodo.
                print(f"Elemento {nodoActual.getDato()} eliminado con éxito al final de la lista")

        else:
            print("No se puede eliminar el elemento, la lista está vacía.")

    def eliminarAntes(self, criterio):
        """
        Elimina el nodo antes del nodo que cumple con el criterio.
        :param criterio: Valor del nodo que se tomará como referencia para eliminar el nodo anterior.
        """
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:
                print("No se puede eliminar, la lista solo tiene un elemento.")
            elif self.__cabeza.getSig().getDato() == criterio:
                # Si el nodo antes del criterio es la cabeza, eliminar la cabeza.
                self.eliminarInicio()
            else:
                nodoActual = self.__cabeza
                # Busca el nodo antes del nodo cuyo siguiente es el criterio.
                while nodoActual.getSig().getSig().getDato() != criterio:
                    if nodoActual.getSig() is not None:
                        nodoActual = nodoActual.getSig()
                nodoEliminar = nodoActual.getSig()
                nodoActual.setSig(nodoEliminar.getSig())
                nodoEliminar.setSig(None)
                print(f"Elemento {nodoEliminar.getDato()} eliminado con éxito antes de {criterio}")

        else:
            print("No se puede eliminar el elemento, la lista está vacía.")

    def eliminarDespues(self, criterio):
        """
        Elimina el nodo después del nodo que cumple con el criterio.
        :param criterio: Valor del nodo que se tomará como referencia para eliminar el nodo siguiente.
        """
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:
                print("No se puede eliminar, la lista solo tiene un elemento.")
            elif self.__cabeza.getDato() == criterio:
                # Si el criterio es la cabeza, eliminar el nodo siguiente.
                self.eliminarFinal()
            else:
                nodoActual = self.__cabeza
                # Busca el nodo con el criterio dado.
                while nodoActual.getDato() != criterio:
                    if nodoActual.getSig() is not None:
                        nodoActual = nodoActual.getSig()
                nodoEliminar = nodoActual.getSig()
                nodoActual.setSig(nodoEliminar.getSig())
                nodoEliminar.setSig(None)
                print(f"Elemento {nodoEliminar.getDato()} eliminado con éxito después de {criterio}")
        else:
            print("No se puede eliminar el elemento, está vacía la lista.")


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
