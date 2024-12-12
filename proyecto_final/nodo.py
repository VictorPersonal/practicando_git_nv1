from tkinter import *
from tkinter import messagebox
class Nodo:
    def __init__(self, nombre, tipo, padre=None):
        self.nombre = nombre
        self.tipo = tipo
        self.hijos = [] if tipo == "carpeta" else None
        self.padre = padre



    def agregar_hijo_interfaz(self, nodo):
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
        return f"{self.nombre} ({self.tipo})"