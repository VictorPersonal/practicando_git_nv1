__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"
class Bodega:
    """
    Clase que representa una bodega para almacenar y gestionar elementos.
    """

    def __init__(self):
        """
        Inicializa una bodega con una lista vacía de elementos.
        """
        self.elementos = []

    def agregar_elemento(self, elemento):
        """
        Agrega un elemento a la lista de elementos de la bodega.

        Args:
            elemento: El objeto que representa el elemento a agregar.
        """
        self.elementos.append(elemento)

    def merge_sort(self, arr, key):
        """
        Ordena una lista utilizando el algoritmo merge sort con un criterio especificado.

        Args:
            arr: Lista de elementos a ordenar.
            key: Función que define el criterio de comparación.

        Returns:
            Una lista ordenada según el criterio proporcionado.
        """
        if len(arr) == 1:
            return arr

        medio = len(arr) // 2
        arr_izquierda = arr[:medio]
        arr_derecha = arr[medio:]

        arr_izquierda_ordenado = self.merge_sort(arr_izquierda, key)
        arr_derecha_ordenado = self.merge_sort(arr_derecha, key)

        return self.merge(arr_izquierda_ordenado, arr_derecha_ordenado, key)

    def merge(self, arr_izquierda, arr_derecha, key):
        """
        Combina dos listas ordenadas en una única lista ordenada.

        Args:
            arr_izquierda: Primera lista ordenada.
            arr_derecha: Segunda lista ordenada.
            key: Función que define el criterio de comparación.

        Returns:
            Lista combinada y ordenada.
        """
        arr_resultado = []
        while len(arr_izquierda) > 0 and len(arr_derecha) > 0:
            if key(arr_izquierda[0]) > key(arr_derecha[0]):
                arr_resultado.append(arr_derecha[0])
                arr_derecha.pop(0)
            else:
                arr_resultado.append(arr_izquierda[0])
                arr_izquierda.pop(0)

        while len(arr_izquierda) > 0:
            arr_resultado.append(arr_izquierda[0])
            arr_izquierda.pop(0)

        while len(arr_derecha) > 0:
            arr_resultado.append(arr_derecha[0])
            arr_derecha.pop(0)

        return arr_resultado

    def ordenar_por_valor_descendente(self):
        """
        Ordena los elementos de la bodega en orden descendente por su valor.
        """
        self.setElementos(self.merge_sort(self.getElementos(), key=lambda e: -e.getValor()))

    def ordenar_por_peso_ascendente(self):
        """
        Ordena los elementos de la bodega en orden ascendente por su peso.
        """
        self.setElementos(self.merge_sort(self.getElementos(), key=lambda e: e.getPeso()))

    def getElementos(self):
        """
        Obtiene la lista de elementos almacenados en la bodega.

        Returns:
            Una lista de elementos en la bodega.
        """
        return self.elementos

    def setElementos(self, elementos):
        """
        Establece la lista de elementos de la bodega.

        Args:
            elementos: Una nueva lista de elementos a almacenar.
        """
        self.elementos = elementos
