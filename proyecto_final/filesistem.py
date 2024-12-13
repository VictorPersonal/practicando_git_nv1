from nodo import Nodo
class FileSystem:
    """
    Representa el sistema de archivos. Contiene la raíz y el directorio actual,
    y permite operaciones como crear, listar, eliminar, cambiar de directorio y buscar nodos.

    Atributos:
        raiz (Nodo): El nodo raíz del sistema de archivos (por defecto, "C:/").
        directorio_actual (Nodo): El directorio actualmente activo o donde el usuario se encuentra.

    Métodos:
        crear(nombre, tipo): Crea un nodo de tipo archivo o carpeta en el directorio actual.
        listar(): Devuelve una cadena con los nodos en el directorio actual.
        eliminar(nombre): Elimina un nodo (archivo o carpeta) del directorio actual.
        cambiar_directorio(nombre): Cambia el directorio actual a uno especificado.
        buscar(nombre, nodo_actual): Busca un nodo por nombre dentro del sistema de archivos.
        __str__(): Representa el sistema de archivos como una cadena.
    """

    def __init__(self):
        """
        Inicializa el sistema de archivos con un nodo raíz "C:/" y establece el directorio actual como la raíz.
        """
        self.raiz = Nodo("C:/", "carpeta")
        self.directorio_actual = self.raiz  # El directorio actual hace referencia a la raíz inicialmente

    def crear(self, nombre, tipo):
        """
        Crea un nodo de tipo archivo o carpeta dentro del directorio actual.

        Args:
            nombre (str): El nombre del nodo a crear.
            tipo (str): El tipo de nodo, ya sea "carpeta" o "archivo".

        Returns:
            bool: Retorna True si el nodo fue creado correctamente.
        
        Llama al método 'agregar_hijo_interfaz' del directorio actual para agregar el nuevo nodo.
        """
        nuevo_nodo = Nodo(nombre, tipo, self.directorio_actual)
        return self.directorio_actual.agregar_hijo_interfaz(nuevo_nodo)

    def listar(self):
        """
        Lista los nodos en el directorio actual.

        Returns:
            str: Una cadena que describe el directorio actual y sus elementos.
        
        Si el directorio está vacío, se indica con un mensaje apropiado.
        """
        resultado = []
        if self.directorio_actual.hijos:
            for hijo in self.directorio_actual.hijos:
                resultado.append(str(hijo))
        else:
            resultado = ["El directorio actual está vacío"]
        
        contenido = "\n".join(resultado)
        return f"El directorio en el que se encuentra es: {self.directorio_actual}\n{contenido}"

    def eliminar(self, nombre):
        """
        Elimina un nodo (archivo o carpeta) del directorio actual.

        Args:
            nombre (str): El nombre del nodo a eliminar.

        Lanza un ValueError si el nodo no se encuentra.
        Si es una carpeta con hijos, elimina recursivamente los hijos.
        """
        for hijo in self.directorio_actual.hijos:
            if hijo.nombre == nombre:
                if hijo.tipo == "carpeta" and hijo.hijos:
                    hijo.hijos = []  # Eliminar todos los hijos si es una carpeta
                self.directorio_actual.hijos.remove(hijo)
                print(f"El nodo {nombre} ha sido eliminado.")
                return
        raise ValueError(f"No se encontró el nodo {nombre} en el directorio actual.")

    def cambiar_directorio(self, nombre):
        """
        Cambia el directorio actual a uno especificado.

        Args:
            nombre (str): El nombre del directorio al que se desea cambiar.
        
        Lanza un ValueError si el directorio no existe o si se intenta subir más allá de la raíz.
        """
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
        """
        Representa el sistema de archivos como una cadena.
        
        Returns:
            str: Una cadena representando el directorio actual.
        """
        return f"Directorio actual: {self.directorio_actual.nombre}"

    def buscar(self, nombre, nodo_actual=None):
        """
        Busca un nodo por nombre en el árbol de directorios.

        Args:
            nombre (str): Nombre del nodo a buscar.
            nodo_actual (Nodo, opcional): Nodo desde donde iniciar la búsqueda. Por defecto es la raíz.

        Returns:
            Nodo: El nodo encontrado o None si no se encuentra.
        
        La búsqueda se realiza de manera recursiva a través de los hijos de los nodos.
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
