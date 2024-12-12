# Implementación de las clases Nodo y FileSystem
from nodo import Nodo


class FileSystem:
    def __init__(self):
        self.raiz = Nodo("C:/", "carpeta")
        self.directorio_actual = self.raiz #Hace referencia al nodo


    def crear(self, nombre, tipo):
        nuevo_nodo = Nodo(nombre, tipo, self.directorio_actual)
        return self.directorio_actual.agregar_hijo_interfaz(nuevo_nodo)

    def listar(self):
        resultado=[]
        if self.directorio_actual.hijos:
            for hijo in self.directorio_actual.hijos:
                resultado.append(str(hijo))
            

        else:
            resultado=["El directorio actual está vacio"]

        
        contenido="\n".join(resultado)
        return f"El directorio en el que se encuentra es: {self.directorio_actual}\n{contenido}"


    def eliminar(self, nombre):
            """
            Elimina una carpeta o archivo del directorio actual.
            Si es una carpeta, se eliminarán sus hijos también.
            :param nombre: Nombre del archivo o carpeta a eliminar.
            """
            for hijo in self.directorio_actual.hijos:
                if hijo.nombre == nombre:
                    if hijo.tipo == "carpeta" and hijo.hijos:
                        # Si es una carpeta con hijos, eliminarlos recursivamente
                        hijo.hijos = []  # Eliminar todos los hijos
                    self.directorio_actual.hijos.remove(hijo)
                    
                    print(f"El nodo {nombre} ha sido eliminado.")
                    return
            raise ValueError(f"No se encontró el nodo {nombre} en el directorio actual.")


    
    def cambiar_directorio(self, nombre):
        if nombre == "..":
            if self.directorio_actual.padre:
                self.directorio_actual = self.directorio_actual.padre
                return  # Cambio exitoso
            else:
                raise ValueError("Ya estás en la raíz.")  # No se puede subir más allá de la raíz

        for hijo in self.directorio_actual.hijos:
            if hijo.nombre == nombre and hijo.tipo == "carpeta":
                self.directorio_actual = hijo
                return  # Cambio exitoso

        # Si el directorio no existe o no es una carpeta
        raise ValueError(f"No existe una carpeta llamada '{nombre}' en el directorio actual.")

    def __str__(self):
        return f"Directorio actual: {self.directorio_actual.nombre}"
    

    def buscar(self, nombre, nodo_actual=None):
        """
        Busca un nodo por nombre en el árbol de directorios.
        :param nombre: Nombre del nodo a buscar.
        :param nodo_actual: Nodo desde donde iniciar la búsqueda (por defecto es la raíz).
        :return: Nodo encontrado o None si no se encuentra.
        """
        if nodo_actual is None:
            nodo_actual = self.raiz  # Comienza desde la raíz

        if nodo_actual.nombre == nombre:
            return nodo_actual

        if nodo_actual.hijos:
            for hijo in nodo_actual.hijos:
                resultado = self.buscar(nombre, hijo)
                if resultado:
                    return resultado

        return None




