__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"


from bodega import Bodega
from flota import Flota
from elemento import Elemento
from camion import Camion

class Main():
    """
    Clase principal que contiene los métodos para interactuar con la bodega y la flota.
    Proporciona un menú para realizar diversas operaciones como agregar elementos, 
    gestionar camiones y mostrar información.
    """
    def agregar_elemento_bodega(bodega):
        """
        Agrega un nuevo elemento a la bodega solicitando los datos al usuario.

        Args:
            bodega: Instancia de la clase Bodega donde se agregará el elemento.
        """
        nombre = input("Nombre del elemento: ")
        peso = int(input("Peso del elemento: "))
        valor = int(input("Valor del elemento: "))
        elemento = Elemento(nombre, peso, valor)  # Código generado automáticamente
        bodega.agregar_elemento(elemento)
        print(f"Elemento agregado a la bodega con Código: {elemento.getCodigo()}")
    
    def agregar_camion_flota(flota):
        """
        Agrega un nuevo camión a la flota solicitando los datos al usuario.

        Args:
            flota: Instancia de la clase Flota donde se agregará el camión.
        """
        placa = input("Placa del camión: ")
        modelo = input("Modelo del camión: ")
        marca = input("Marca del camión: ")
        camion = Camion(placa, modelo, marca)
        flota.agregar_camion(camion)
        print("Camión agregado a la flota.")

    def llenar_camiones(flota, bodega):
        
        """
        Llena los camiones de la flota con los elementos de la bodega, 
        distribuyendo la carga de manera equilibrada.

        Args:
            flota: Instancia de la clase Flota que contiene los camiones.
            bodega: Instancia de la clase Bodega que contiene los elementos.
        """
        
        if not flota.getCamiones():
            print("No hay camiones en la flota.")
        elif not bodega.getElementos():
            print("No hay elementos en la bodega.")
        else:
            flota.llenar_camiones(bodega)
            print("Los camiones han sido llenados.")

    def mostrar_camiones(flota):

        """
        Muestra la información de los camiones en la flota, incluyendo su carga,
        peso total y valor total.

        Args:
            flota: Instancia de la clase Flota que contiene los camiones.
        """

        for camion in flota.getCamiones():
            print(f"\n{camion}")
            print(f"Carga: {camion.getCarga()}")
            print(f"Peso total: {camion.getPesoTotal()}")
            print(f"Valor total: {camion.getValorTotal()}")

    def mostrar_bodega(bodega):
        
        """
        Muestra los elementos restantes en la bodega.

        Args:
            bodega: Instancia de la clase Bodega que contiene los elementos.
        """

        if not bodega.getElementos():
            print("La bodega está vacía.")
        else:
            print("Elementos restantes en bodega:")
            for elemento in bodega.getElementos():
                print(elemento)

    def main():

        """
        Método principal que ejecuta el programa. 
        Muestra un menú interactivo para gestionar la bodega y la flota.
        """

        bodega = Bodega()
        flota = Flota()
        opcion = 9999
        while opcion != 0:
            opcion = int(input("---MENÚ PRINCIPAL---\n1. Agregar Elemento a la Bodega.\n2. Agregar Camión a la Flota.\n3. Llenar Camiones.\n4. Mostrar Camiones y sus Cargas.\n5. Mostrar Elementos Restantes en Bodega.\n0. Salir.\n-> "))
            if opcion == 1:
                Main.agregar_elemento_bodega(bodega)
            elif opcion == 2:
                Main.agregar_camion_flota(flota)
            elif opcion == 3:
                Main.llenar_camiones(flota, bodega)
            elif opcion == 4:
                Main.mostrar_camiones(flota)
            elif opcion == 5:
                Main.mostrar_bodega(bodega)
            elif opcion == 0:
                print("Hasta Pronto :D")
                break
            else:
                print("Opción Incorrecta, intente nuevamente.")
            
Main.main()
