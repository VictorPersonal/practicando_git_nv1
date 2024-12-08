
class Nodo:
    def __init__(self, nombre, tipo, padre=None):
        self.nombre = nombre
        self.tipo = tipo
        self.hijos = [] if tipo == "carpeta" else None
        self.padre = padre

    def agregar_hijo(self, nodo):
        if self.tipo != "carpeta":
            raise ValueError("Solo las carpetas pueden tener hijos.")
        for hijo in self.hijos:
            if hijo.nombre == nodo.nombre:
                raise ValueError(f"Ya existe un elemento llamado {nodo.nombre}.")
        self.hijos.append(nodo)


    def __str__(self):
        return f"{self.nombre} ({self.tipo})"