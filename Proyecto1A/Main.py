__author__="VISANI"
__copyrigth__="Copyrigth 2024, VISANI"
__credits__=["VISANI","Victor Tabares","Santiago Giraldo Patiño","Alison Tatiana Chamorro Jimenez"]
__licence__="GPS"
__version__="0.10.1"
__maintainer__="VISANI"
__email__="alison.chamorro@correounivalle.edu.co"
__status__="Prueba"

from AgregarFinal import AgregarFinal
from ReclamarSubsidio import ReclamarSubsidio
from Lista import Lista
from Persona import Persona
import random
import sys
class Main(): 
    """Esta clase es el centro de todo el laboratorio, y nos ayuda a que todo esté mucho más ordenado.
    """
    def main():
        """Este método simula un menú interactivo en el cual podemos controlar todo lo que tiene que ver con el laboratorio.
        """
        nombres = ["Ana", "Juan", "Luis", "María", "Carlos", "Sofía", "Diego", "Lucía", "Miguel", "Laura"] #1
        miLista = Lista()#2
        miPersona = Persona(random.choice(nombres), random.randint(5, 17))#3
        agregar = AgregarFinal(miLista)#2
        reclamar = ReclamarSubsidio(miLista)#3 --> Pendiente, ELLOS LA HACEN
        opcion = 9999 #1
        while opcion != 0: #n+1 --->> 10n^2+69n+59
            opcion = int(input("\n--- MENÚ PRINCIPAL ---\n"
                               "1. Imprimir Lista.\n"
                               "2. Agregar Personas.\n"
                               "3. Reclamar Subsidio.\n"
                               "4. Personas Que Retiraron.\n"
                               "5. Total Dinero Entregado.\n"
                               "0. Salir.\n"
                               "-> "))#3(n+1) --> 3n+3
            if opcion == 1:#1(n+1) --> n+1 --> 5n^2+15n+n+10+1 --> 5n^2+16n+11

                miLista.imprimirLista()#(n+1)(5n+10) --> 5n^2+10n+5n+10 --> 5n^2+15n+10
                
            elif opcion == 2:#1(n+1) --> n+1 --> 5n^2+16n+11

                for i in range(50):#2n+2 --> (5n+10)(n+1) --> 5n^2+5n+10n+10 --> 5n^2+15n+10
                    agregar.agregarFinalLista(miPersona)#(3n+8)


            elif opcion == 3:#1(n+1) --> 21n+n+1+21 --> 22n+22

                reclamar.reclamarSubsidio() #21(n+1)  --> 21n+21           #Colocar la complejidad de la función


            elif opcion == 4:#1(n+1) --> n+1 --> 2n+n+1+2 --> 3n+3

                reclamar.contarPersonas() #2*(n+1) -->  2n+2   #Colocar la complejidad del método



            elif opcion == 5:#1(n+1) 8n+n+8+1 --> 9n+9

                reclamar.contarDinero() #8*(n+1) -->   8n+8      #Colocar la complejidad de la función y multiplicarlo con n+1

            elif opcion == 0:#1(n+1) --> n+1 --> n+n+1+1 --> 2n+2

                print("Hasta Pronto!!! /( ._.)/")#1(n+1) --> n+1

            else:
                print("Opcion incorrecta, por favor intente nuevamente ⤜(ʘ_ʘ)⤏")#1(n+1) --> n+1
Main.main()

#5n^2+16n+11+5n^2+16n+11+22n+22+3n+3+9n+9+2n+2+n+1


#5n^2+5n^2 --> 10n^2
#16n+16n+22n+3n+9n+2n+n --> 69n
#11+11+22+3+9+2+1 --> 59

#Complejidades
#O(n)= 10n^2+69n+59+1+2+3+2+3+1 = O(n)==> 10n^2+69n+71 --> O(n)=n^2
#S(n)= 2720 bytes