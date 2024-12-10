
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
                #Validar si quiere reemplazar al archivo
                respuesta=input(f"El elemento {nodo.nombre} ya existe. ¿Desea reemplazarlo? (s/n): ").strip().lower()
                if (respuesta == 's'):#Si lo reemplaza
                    self.hijos.remove(hijo)#Se borra el anterior y se agrega este.
                    print(f"El elemento {nodo.nombre} ha sido reemplazado.")
                else:
                    #Si la respuesta es NO entonces se conserva el anterior y se borra el que se quizo eliminar
                    print(f"El elemento {nodo.nombre} no fue reemplazado.")
                    return #Importante para evitar que el segundo archivo creado, con el mismo nombre se guarde
                
        self.hijos.append(nodo)


    def __str__(self):
        return f"{self.nombre} ({self.tipo})"