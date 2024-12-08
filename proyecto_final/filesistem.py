# Implementación de las clases Nodo y FileSystem
from nodo import Nodo


class FileSystem:
    def __init__(self):
        self.raiz = Nodo("C:/", "carpeta")
        self.directorio_actual = self.raiz #Hace referencia al nodo

    def crear(self, nombre, tipo):
        nuevo_nodo = Nodo(nombre, tipo, self.directorio_actual)
        self.directorio_actual.agregar_hijo(nuevo_nodo)

    def listar(self):
        if self.directorio_actual.hijos:
            for hijo in self.directorio_actual.hijos:
                print(hijo)
        else:
            print("El directorio actual está vacío.")

    def eliminar(self, nombre):
        """
        Elimina una carpeta o archivo del directorio actual.
        Si es una carpeta, se eliminarán sus hijos también.
        :param nombre: Nombre del archivo o carpeta a eliminar.
        """
        for hijo in self.directorio_actual.hijos: #como self.directorio_actual hace referencia a un nodo entonces se puede acceder a la lista definida dentro de los atributos de la clase Nodo como lo es self.hijos.
            if hijo.nombre == nombre:
                if hijo.tipo == "carpeta" and hijo.hijos:
                    # Si es una carpeta con hijos, eliminarlos recursivamente
                    hijo.hijos = []  # Eliminar todos los hijos
                self.directorio_actual.hijos.remove(hijo)
                print(f"El nodo {nombre} ha sido eliminado.")
                return
        print(f"No se encontró el nodo {nombre} en el directorio actual.")

    def cambiar_directorio(self, nombre):
        if nombre == "..":
            if self.directorio_actual.padre: #como self.directorio_actual hace referencia a un nodo entonces se puede acceder los atributos de la clase Nodo como lo es self.padre.
                self.directorio_actual = self.directorio_actual.padre
            else:
                print("Ya estás en la raíz.")
            return

        for hijo in self.directorio_actual.hijos:
            if hijo.nombre == nombre and hijo.tipo == "carpeta":
                self.directorio_actual = hijo
                return
        print(f"No existe una carpeta llamada {nombre} en el directorio actual.")

    def __str__(self):
        return f"Directorio actual: {self.directorio_actual.nombre}"
    

    def buscar(self, nombre):
        """
        Busca un archivo o carpeta en todo el sistema de archivos.
        :param nombre: Nombre del archivo o carpeta a buscar.
        :return: El nodo encontrado o un mensaje si no se encuentra.
        """
        def buscar_recursivo(nodo, nombre):
            if nodo.nombre == nombre:
                return nodo
            if nodo.tipo == "carpeta":
                for hijo in nodo.hijos:
                    resultado = buscar_recursivo(hijo, nombre)
                    if resultado:
                        return resultado
            return None

        resultado = buscar_recursivo(self.raiz, nombre)
        if resultado:
            print(f"Se encontró el nodo: {resultado}")
        else:
            print(f"No se encontró el nodo con nombre {nombre}.")






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
            print(f"No se encontró el nodo {nombre} en el directorio actual.")



"""fs=FileSystem()
fs.crear("documentos", "carpeta")
fs.crear("foto.jpg", "archivo")
fs.crear("videos", "carpeta")
fs.listar()

fs.cambiar_directorio("documentos")
fs.crear("informe.docx", "archivo")
fs.listar()

fs.eliminar("informe.docx")
fs.listar()

fs.cambiar_directorio("..")
fs.buscar("foto.jpg")
fs.eliminar("foto.jpg")
fs.listar()
"""
