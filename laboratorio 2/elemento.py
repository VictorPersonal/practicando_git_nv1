__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

class Elemento:
    """
    Clase que representa un elemento con nombre, peso, valor y un código único.
    """
    contador_codigo = 1

    def __init__(self, nombre, peso, valor):
        """
        Inicializa un nuevo elemento con nombre, peso y valor. 
        El código único se asigna automáticamente.

        Args:
            nombre: El nombre del elemento.
            peso: El peso del elemento.
            valor: El valor del elemento.
        """
        self.setCodigo(Elemento.contador_codigo)
        Elemento.contador_codigo += 1
        self.setNombre(nombre)
        self.setPeso(peso)
        self.setValor(valor)

    def __repr__(self):
        """
        Representación en cadena del elemento.

        Returns:
            Una cadena que describe el elemento con su nombre, código, peso y valor.
        """
        return f"{self.getNombre()} (Código: {self.getCodigo()}, Peso: {self.getPeso()}, Valor: {self.getValor()})"

    def getCodigo(self):
        """
        Obtiene el código único del elemento.

        Returns:
            El código único del elemento.
        """
        return self.codigo

    def getNombre(self):
        """
        Obtiene el nombre del elemento.

        Returns:
            El nombre del elemento.
        """
        return self.nombre

    def getPeso(self):
        """
        Obtiene el peso del elemento.

        Returns:
            El peso del elemento.
        """
        return self.peso

    def getValor(self):
        """
        Obtiene el valor del elemento.

        Returns:
            El valor del elemento.
        """
        return self.valor

    def setCodigo(self, codigo):
        """
        Establece el código único del elemento.

        Args:
            codigo: El nuevo código único del elemento.
        """
        self.codigo = codigo

    def setNombre(self, nombre):
        """
        Establece el nombre del elemento.

        Args:
            nombre: El nuevo nombre del elemento.
        """
        self.nombre = nombre

    def setPeso(self, peso):
        """
        Establece el peso del elemento.

        Args:
            peso: El nuevo peso del elemento.
        """
        self.peso = peso

    def setValor(self, valor):
        """
        Establece el valor del elemento.

        Args:
            valor: El nuevo valor del elemento.
        """
        self.valor = valor
