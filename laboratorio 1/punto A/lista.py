from nodo import Nodo
class Lista():
    def __init__(self):
        self.cabeza = None

    def getCabeza(self):
        return self.cabeza
    
    def setCabeza(self, cabeza):
        self.cabeza = cabeza

    def validarListaVacia(self,dato):
        if self.cabeza is None:
            nuevoNodo=Nodo(dato)
            self.cabeza=nuevoNodo
            return True
        return False
    
    
    def agregarFinal(self, dato):
        if self.validarListaVacia(dato):
            return
        else:
            nuevoNodo = Nodo(dato)
            actual = self.cabeza
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nuevoNodo)

    
    def eliminarInicio(self):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            nodo_eliminar = self.cabeza
            self.cabeza = nodo_eliminar.getSiguiente()  # Actualiza la cabeza al siguiente nodo
            nodo_eliminar.setSiguiente(None)  # Desconecta el nodo eliminado para que el recolector de basura lo libere

            
            

    
    def mostrarLista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()