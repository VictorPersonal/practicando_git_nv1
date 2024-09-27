from nodo import Nodo

class Lista:
    """
    Esta clase implementa una lista enlazada simple. Una lista enlazada es una estructura de datos donde cada elemento
    (nodo) contiene un valor y una referencia al siguiente nodo en la lista. Esta clase tiene dos atributos principales:
    'cabeza' que representa el primer nodo de la lista, y 'cola' que representa el último nodo.
    """

    def __init__(self):
        """
        Inicializa una lista vacía. La cabeza y la cola de la lista se establecen en None, lo que significa que no hay
        nodos en la lista al principio.
        """
        self.__cabeza = None
        self.__cola = None

    def getCabeza(self):
#Consultar puntero con get
        """
        Obtiene el nodo que está al inicio de la lista (cabeza).
        """
        return self.__cabeza

    def setCabeza(self, cabeza):
#Asignar puntero con set
        """
        Establece la cabeza de la lista en un nodo específico.
        :param cabeza: El nodo que se establecerá como cabeza de la lista.
        """
        self.__cabeza = cabeza

    def getCola(self):
        """
        Obtiene el nodo que está al final de la lista (cola).
        """
        return self.__cola

    def setCola(self, cola):
        """
        Establece la cola de la lista en un nodo específico.
        :param cola: El nodo que se establecerá como cola de la lista.
        """
        self.__cola = cola

    def validarListaVacia(self, dato):
        """
        Verifica si la lista está vacía. Si está vacía, agrega un nuevo nodo con el dato proporcionado y actualiza tanto
        la cabeza como la cola para que apunten a ese nuevo nodo.
        :param dato: El valor del nuevo nodo que se va a agregar.
        :return: True si la lista estaba vacía y se agregó el nodo, False en caso contrario.
        """
        if self.__cabeza is None and self.__cola is None:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo con el dato proporcionado.
            self.__cabeza = nuevoNodo  # El nuevo nodo será la cabeza de la lista.
            self.__cola = nuevoNodo  # El nuevo nodo también será la cola de la lista.
            print("Primer Dato {} agregado a la lista con éxito".format(dato))
            return True
        return False

    def agregarInicio(self, dato):
        """
        Agrega un nuevo nodo al inicio de la lista. Si la lista está vacía, se usa 'validarListaVacia' para agregar el
        nodo. Si no está vacía, el nuevo nodo se coloca antes de la cabeza actual.
        :param dato: El valor del nuevo nodo que se va a agregar.
        """
        if self.validarListaVacia(dato):
            pass
        else:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo.
            nuevoNodo.setSig(self.__cabeza)  # Apuntar al nodo que era la cabeza como el siguiente del nuevo nodo.
            self.__cabeza = nuevoNodo  # Actualizar la cabeza de la lista.
            print("Dato {} agregado al inicio de la lista con éxito".format(dato))

    def agregarFinal(self, dato):
        """
        Agrega un nuevo nodo al final de la lista. Si la lista está vacía, se usa 'validarListaVacia'. Si no, el nuevo
        nodo se coloca después del nodo que es actualmente la cola.
        :param dato: El valor del nuevo nodo que se va a agregar.
        """
        if self.validarListaVacia(dato):
            pass
        else:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo.
            self.__cola.setSig(nuevoNodo)  # El nodo actual en la cola apunta al nuevo nodo.
            self.__cola = nuevoNodo  # Actualizar la cola de la lista.
            print("Dato {} agregado al final de la lista con éxito".format(dato))

    def agregarAntes(self, dato, criterio):
        """
        Agrega un nuevo nodo antes de un nodo específico basado en el criterio (dato) proporcionado. 
        Si la lista está vacía, se usa 'validarListaVacia'.
        :param dato: El valor del nuevo nodo que se va a agregar.
        :param criterio: El valor del nodo antes del cual se insertará el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            pass
        elif self.__cabeza.getDato() == criterio:
            self.agregarInicio(dato)
        else:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo.
            nodoActual = self.__cabeza  # Comenzar desde la cabeza de la lista.
            while nodoActual.getSig().getDato() != criterio:  # Buscar el nodo antes del cual se insertará el nuevo nodo.
                if nodoActual.getSig() != None:
                    nodoActual = nodoActual.getSig()
                else:
                    break
            nuevoNodo.setSig(nodoActual.getSig())  # El nuevo nodo apunta al nodo que seguía al actual.
            nodoActual.setSig(nuevoNodo)  # El nodo actual apunta al nuevo nodo.
            print("Dato {} agregado a la lista antes de {} con éxito".format(dato,criterio))

    def agregarDespues(self, dato, criterio):
        """
        Agrega un nuevo nodo después de un nodo específico basado en el criterio (dato) proporcionado.
        :param dato: El valor del nuevo nodo que se va a agregar.
        :param criterio: El valor del nodo después del cual se insertará el nuevo nodo.
        """
        if self.validarListaVacia(dato):
            pass
        else:
            nuevoNodo = Nodo(dato)  # Crear un nuevo nodo.
            nodoActual = self.__cabeza  # Comenzar desde la cabeza de la lista.
            while nodoActual.getDato() != criterio:  # Buscar el nodo después del cual se insertará el nuevo nodo.
                if nodoActual.getSig() != None:
                    nodoActual = nodoActual.getSig()
                else:
                    break
            nuevoNodo.setSig(nodoActual.getSig())  # El nuevo nodo apunta al nodo que seguía al actual.
            nodoActual.setSig(nuevoNodo)  # El nodo actual apunta al nuevo nodo.
            if nodoActual == self.__cola:
                self.__cola = nuevoNodo
            print("Dato {} agregado a la lista después de {} con éxito".format(dato,criterio))

    def eliminarInicio(self):
        """
        Elimina el primer nodo de la lista (la cabeza). La cabeza se actualiza para que apunte al segundo nodo de la lista.
        Si solo hay un nodo, la lista quedará vacía.
        """
        if self.__cabeza != None:
            if self.__cabeza == self.__cola:  # Si solo hay un nodo.
                self.__cabeza = None
                self.__cola = None
                print("Elemento eliminado exitosamente, la lista está vacía.")

            else:
                nodoActual = self.__cabeza  # Guardar la cabeza actual.
                self.__cabeza = self.__cabeza.getSig()  # Actualizar la cabeza para que sea el siguiente nodo.
                print("Elemento {} eliminado con éxito al inicio de la lista".format(nodoActual.getSig().getDato()))
                nodoActual.setSig(None)  # Eliminar la referencia del nodo que era la cabeza.


        else:
            print("No se puede eliminar el elemento, está vacía la lista.")

    def eliminarFinal(self):
        """
        Elimina el último nodo de la lista (la cola). Si la lista solo tiene un nodo, la cabeza y la cola se establecen
        en None, lo que vacía la lista.
        """
        if self.__cabeza is not None:
            if self.__cabeza == self.__cola:  # Si solo hay un nodo.
                self.__cabeza = None
                self.__cola = None
            else:
                nodoActual = self.__cabeza  # Comenzar desde la cabeza de la lista.
                while nodoActual.getSig() != self.__cola:  # Buscar el penúltimo nodo.
                    nodoActual = nodoActual.getSig()
                self.__cola = nodoActual  # Actualizar la cola para que sea el penúltimo nodo.
                nodoActual.setSig(None)  # Eliminar la referencia al último nodo.
                print("Elemento {} eliminado con éxito al inicio de la lista".format(nodoActual.getDato()))

        else:
            print("No se puede eliminar el elemento, está vacía la lista.")


    def eliminarMedioAntesDelCriterio(self, criterio):
        """
        Elimina un nodo ubicado en el medio de la lista que precede a otro nodo
        que coincide con el 'criterio' proporcionado. Requiere que existan al menos
        dos nodos en la lista.
        
        :param criterio: El valor del nodo que sigue al nodo que será eliminado.
        """
        # No tiene elementos: 
        if self.__cabeza is None:
            print("La lista está vacía.")
            return

        # Si solo hay un nodo.
        if self.__cabeza == self.__cola:
            self.__cabeza = None
            self.__cola = None
            print("Se eliminó el único nodo en la lista.")
            return

        nodoActual = self.__cabeza

        # Recorremos la lista si tiene más de un nodo y eliminamos según el criterio.
        while nodoActual.getSig() is not None and nodoActual.getSig().getSig() is not None:
            # Verificamos si el segundo nodo después del actual (nodoActual.sig.sig) coincide con el criterio.
            if nodoActual.getSig().getSig().getDato() == criterio:
                nodoEliminar = nodoActual.getSig()  # El nodo que queremos eliminar.
                nodoActual.setSig(nodoEliminar.getSig())  # Saltamos el nodo a eliminar.
                nodoEliminar.setSig(None)  # Desconectamos el nodo eliminado.
                print(f"Se eliminó el nodo con el dato: {nodoEliminar.getDato()}.")
                return  # Nodo eliminado, salimos del método.
            
            nodoActual = nodoActual.getSig()  # Avanzamos al siguiente nodo.

        print("No se encontró el nodo con el criterio especificado.")


    def eliminarMedioDespuesDelCriterio(self, criterio):
        nodoActual = self.__cabeza

        # Verificar si la lista está vacía
        if self.validarListaVacia(criterio):
            print("La lista está vacía, no se puede eliminar ningún nodo.")
            return

        # Buscar el nodo que contiene el criterio
        while nodoActual is not None and nodoActual.getDato() != criterio:
            nodoActual = nodoActual.getSig()

        # Verificar si se encontró el nodo con el criterio
        if nodoActual is None:
            print("No se encontró el nodo con el criterio.")
            return

        # Verificar si hay un nodo después del nodo con el criterio
        if nodoActual.getSig() is None:
            print("No hay nodo después del criterio para eliminar.")
            return

        # Eliminar el nodo siguiente al que contiene el criterio
        nodoEliminar = nodoActual.getSig()  # Nodo a eliminar
        nodoActual.setSig(nodoEliminar.getSig())  # Saltar el nodo a eliminar
        nodoEliminar.setSig(None)  # Desconectar completamente el nodo eliminado
        print(f"Se eliminó el nodo con el dato: {nodoEliminar.getDato()}")

    def eliminarAntes(self, criterio):
        if (self.__cabeza != None):
            if self.__cabeza == self.__cola:
                print("No se puede eliminar elemento debido a que en la lista solo posee 1 dato")
            elif (self.__cabeza.getSig().getDato() == criterio):
                self.eliminarInicio()#Elimino la cabeza
            
            else: #Se sabe que hay mas de 2 nodos
                nodoActual = self.__cabeza
                while nodoActual.getSig().getSig().getDato() != criterio:
                    if nodoActual.getSig != None:
                        nodoActual = nodoActual.getSig()
                nodoEliminar = nodoActual.getSig()
                nodoActual.setSig(nodoEliminar.getSig())
                nodoEliminar.setSig(None)
                print("Elemento {} eliminado con éxito antes de {} de la lista".format(nodoEliminar.getDato(),criterio))

        else:
            print("No se puede eliminar el elemento, está vacía la lista.")

    def eliminarDespues(self, criterio):
        if(self.__cabeza != None):
            if self.__cabeza == self.__cola:
                print("No se puede eliminar elemento debido a que en la lista solo posee 1 dato")
            elif self.__cabeza.getDato() == criterio: #Necesito saber si la cabeza = criterio
                self.eliminarFinal()

            else:
                nodoActual = self.__cabeza
                while nodoActual.getDato() != criterio:
                    if nodoActual.getSig != None:
                        nodoActual = nodoActual.getSig()
                nodoEliminar = nodoActual.getSig()
                nodoActual.setSig(nodoEliminar.getSig())
                nodoEliminar.setSig(None)
                print("Elemento {} eliminado con éxito despues de {} de la lista".format(nodoEliminar.getDato(),criterio))
        else:
            print("No se puede eliminar el elemento, está vacía la lista.")


    def imprimirLista(self):
        if (self.__cabeza != None):
            texto=""
            nodoActual = self.__cabeza
            while (nodoActual != None):
                texto+= str(nodoActual.getDato())+ "->"
                nodoActual=nodoActual.getSig()
            texto += "None"

            print("La lista actual es: "+texto)

        else:
            print("La lista está vacía")