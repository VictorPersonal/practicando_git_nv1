from tkinter import *
from tkinter import messagebox
class Nodo:
    """
    Representa un nodo en el sistema de archivos, que puede ser un archivo o una carpeta.

    Atributos:
        nombre (str): Nombre del nodo (archivo o carpeta).
        tipo (str): Tipo del nodo, ya sea "archivo" o "carpeta".
        hijos (list): Lista de nodos hijos (solo aplica para carpetas).
        padre (Nodo): Nodo padre, es decir, el directorio en el que se encuentra este nodo.

    Métodos:
        agregar_hijo_interfaz(nodo): Permite agregar un nodo hijo al actual, 
                                     solicitando confirmación si el nodo ya existe.
        __str__(): Devuelve una representación en cadena del nodo.
    """

    def __init__(self, nombre, tipo, padre=None):
        """
        Inicializa un nodo con un nombre, tipo y un nodo padre opcional.

        Args:
            nombre (str): Nombre del nodo.
            tipo (str): Tipo del nodo ("archivo" o "carpeta").
            padre (Nodo, opcional): Nodo padre. Por defecto es None.
        """
        self.nombre = nombre
        self.tipo = tipo
        self.hijos = [] if tipo == "carpeta" else None
        self.padre = padre

    def agregar_hijo_interfaz(self, nodo):
        """
        Agrega un nodo hijo al actual. Si un nodo con el mismo nombre ya existe,
        solicita al usuario si desea reemplazarlo.

        Args:
            nodo (Nodo): Nodo hijo a agregar.

        Returns:
            bool: True si el nodo fue agregado o reemplazado, False si el nodo no fue agregado.
        
        Raises:
            ValueError: Si el nodo actual no es una carpeta.
        """
        if self.tipo != "carpeta":
            raise ValueError("Solo las carpetas pueden tener hijos.")

        for hijo in self.hijos:
            if hijo.nombre == nodo.nombre:
                # Preguntar si desea reemplazarlo
                respuesta = messagebox.askquestion("Información", "¿Desea reemplazarlo?")
                if respuesta == 'yes':  # Si acepta reemplazar
                    self.hijos.remove(hijo)
                    self.hijos.append(nodo)  # Agrega el nuevo nodo
                    messagebox.showinfo("Información", f"El elemento {nodo.nombre} ha sido reemplazado.")
                    return True  # Nodo agregado
                else:
                    # Si no desea reemplazar
                    messagebox.showinfo("INFORMACIÓN", f"EL ELEMENTO {nodo.nombre} NO FUE REEMPLAZADO.")
                    return False  # Nodo no agregado

        # Si no hay conflictos, agregar directamente
        self.hijos.append(nodo)
        return True  # Nodo agregado

    def __str__(self):
        """
        Devuelve una representación en cadena del nodo, indicando su nombre y tipo.

        Returns:
            str: Representación en cadena del nodo, como "nombre (tipo)".
        """
        return f"{self.nombre} ({self.tipo})"
