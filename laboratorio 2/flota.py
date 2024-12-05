__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

class Flota:
    """
    Clase que gestiona una flota de camiones, permitiendo agregar camiones y 
    distribuir cargas provenientes de una bodega.
    """

    def __init__(self):
        """
        Inicializa la flota con una lista vacía de camiones.
        """
        self.camiones = []

    def agregar_camion(self, camion):
        """
        Agrega un camión a la flota.

        Args:
            camion (Camion): El camión que se desea agregar.
        """
        self.camiones.append(camion)

    def llenar_camiones(self, bodega):
        """
        Distribuye los elementos de la bodega entre los camiones de la flota, 
        equilibrando el peso en cada camión.

        La distribución considera un peso máximo por camión de 800 unidades. 
        Los elementos se asignan en orden descendente de valor.

        Args:
            bodega (Bodega): La bodega que contiene los elementos a distribuir.
        """
        peso_maximo = 800
        bodega.ordenar_por_valor_descendente()
        elementos = bodega.getElementos()[:]  # Crear una copia de los elementos

        for elemento in elementos:
            # Ordenar camiones por el peso actual para equilibrar las cargas
            camiones_ordenados = sorted(self.getCamiones(), key=lambda c: c.getPesoTotal())

            # Intentar asignar el elemento al primer camión con capacidad disponible
            for camion in camiones_ordenados:
                if camion.getPesoTotal() + elemento.getPeso() <= peso_maximo:
                    camion.cargar_elemento(elemento)
                    bodega.getElementos().remove(elemento)  # Remover el elemento asignado
                    break

    def getCamiones(self):
        """
        Devuelve la lista de camiones en la flota.

        Returns:
            list: Lista de objetos `Camion`.
        """
        return self.camiones

    def setCamiones(self, camiones):
        """
        Establece la lista de camiones para la flota.

        Args:
            camiones (list): Lista de objetos `Camion` que compondrán la flota.
        """
        self.camiones = camiones
