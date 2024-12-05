__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"
class Camion:
    """
    Clase que representa un camión que transporta carga.
    """

    def __init__(self, placa, modelo, marca):
        """
        Inicializa un camión con información básica y sin carga.

        Args:
            placa: La placa del camión.
            modelo: El modelo del camión.
            marca: La marca del camión.
        """
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.carga = []
        self.peso_total = 0
        self.valor_total = 0

    def getPlaca(self):
        """
        Obtiene la placa del camión.

        Returns:
            La placa del camión.
        """
        return self.placa

    def getModelo(self):
        """
        Obtiene el modelo del camión.

        Returns:
            El modelo del camión.
        """
        return self.modelo

    def getMarca(self):
        """
        Obtiene la marca del camión.

        Returns:
            La marca del camión.
        """
        return self.marca

    def getCarga(self):
        """
        Obtiene la carga actual del camión.

        Returns:
            Una lista con los elementos cargados en el camión.
        """
        return self.carga

    def getPesoTotal(self):
        """
        Obtiene el peso total de la carga en el camión.

        Returns:
            El peso total de la carga.
        """
        return self.peso_total

    def getValorTotal(self):
        """
        Obtiene el valor total de la carga en el camión.

        Returns:
            El valor total de la carga.
        """
        return self.valor_total

    def setPlaca(self, placa):
        """
        Establece la placa del camión.

        Args:
            placa: La nueva placa del camión.
        """
        self.placa = placa

    def setModelo(self, modelo):
        """
        Establece el modelo del camión.

        Args:
            modelo: El nuevo modelo del camión.
        """
        self.modelo = modelo

    def setMarca(self, marca):
        """
        Establece la marca del camión.

        Args:
            marca: La nueva marca del camión.
        """
        self.marca = marca

    def setCarga(self, carga):
        """
        Establece la carga del camión.

        Args:
            carga: Una lista de elementos a cargar en el camión.
        """
        self.carga = carga

    def setPesoTotal(self, peso_total):
        """
        Establece el peso total de la carga del camión.

        Args:
            peso_total: El nuevo peso total de la carga.
        """
        self.peso_total = peso_total

    def setValorTotal(self, valor_total):
        """
        Establece el valor total de la carga del camión.

        Args:
            valor_total: El nuevo valor total de la carga.
        """
        self.valor_total = valor_total

    def __repr__(self):
        """
        Representación en cadena del camión.

        Returns:
            Una cadena que describe el camión con su placa, modelo y marca.
        """
        return f"Camión {self.getPlaca()} - Modelo: {self.getModelo()}, Marca: {self.getMarca()}"

    def cargar_elemento(self, elemento):
        """
        Carga un elemento en el camión, actualizando su peso y valor total.

        Args:
            elemento: El objeto que representa el elemento a cargar.
        """
        self.getCarga().append(elemento)
        self.setPesoTotal(self.getPesoTotal() + elemento.getPeso())
        self.setValorTotal(self.getValorTotal() + elemento.getValor())
