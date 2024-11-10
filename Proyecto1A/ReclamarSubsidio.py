__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"
class ReclamarSubsidio:
    """Esta clase representa una o varias acciones que realiza cuando una persona reclama un subsidio.
        Attributes:
            lista(lista)=[lista]
            contador_personas(int)=[contador_personas]
            contador_dinero(float)=[contador_dinero]
    """
    def __init__(self, lista):#3
        """Este método nos permite crear objetos o instancias de la clase ReclamarSubsidio, la cual interactua en el Main.
            Args:
                param1: lista(list)=[lista]
                param2: contador_personas(int)=[0]
                param3: contador_dinero(float)=[0.0]
        """
        self.lista = lista#1
        self.contador_personas = 0#1
        self.contador_dinero = 0.0#1

    def calcularSubsidio(self, edad):#7
        """Este método determina o calcula el monto del subsidio según la edad.
            Args:
                param1: edad(int)=[edad]
            Returns:
                60000(float)
                80000(float)
                100000(float)        
        """
        if 5 <= edad <= 9:#1
            return 60000#1
        elif 10 <= edad <= 13:#1
            return 80000#1
        elif 14 <= edad <= 17:#1
            return 100000#1
        else:
            return 0#1
        

    def reclamarSubsidio(self):#21
        """Este método simula el reclamo del subsidio por una persona y la elimina de la lista.
            Args:
            Returns:
        """
        if self.lista.getCabeza() is None:#1
            print("La lista está vacía :c.")#1
            return#1

        nodo_a_eliminar = self.lista.getCabeza()#2
        persona = nodo_a_eliminar.getDato()#2
        
        # Determina el monto del subsidio según la edad de la persona

        subsidio = self.calcularSubsidio(persona.edad)#8
        self.contador_dinero += subsidio  #1      # Sumar al total de dinero entregado
        self.contador_personas += 1       #1      # Incrementa el contador de personas que han reclamado

        print(f"Subsidio de {subsidio} reclamado por: {persona}")#2

        # Elimina el nodo de la cabeza
        self.lista.setCabeza(nodo_a_eliminar.getSiguiente())#2


    def contarPersonas(self):#2
        """Este método muestra la cantidad de personas que han reclamado su subsidio.
            Args:
        """
        print(f"La cantidad de personas que han retirado el subsidio es de {self.contador_personas} personas.")#2


    def contarDinero(self):#2
        """Este método muestra la cantidad total de dinero entregado en subsidios.
            Args:
        """
        print(f"El total de dinero entregado en subsidios es de {self.contador_dinero} pesos.")#2


