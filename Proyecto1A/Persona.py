__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

class Persona:
    """Esta clase representa a las personas que van a interactuar con todo el sistema para reclamar los subsidios.
        Attributes:
            nombre(str)=[nombre]
            edad(int)=[edad]
    """
    def __init__(self, nombre, edad):
        """Este método nos permite crear objetos o instancias de la clase Persona.
            Args:
                param1: nombre(str)=[nombre]
                param2: edad(int)=[edad]
        """
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """Este método nos permite imprimir o retornar el objeto siendo un string o una cadena directamente.
            Args:
            Returns:
                nombre(str)
                edad(str)
        """
        return f"{self.nombre}, {self.edad} años"
