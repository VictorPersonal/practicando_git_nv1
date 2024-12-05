from lista import Lista
from beneficiario import Beneficiario
import random
class Main():

    def main():
        miBen=Beneficiario("Andres",12)
        miLista = Lista()
        opcion=999
        while (opcion != 0):
            opcion = int(input("\n--- MENÚ PRINCIPAL ---\n"
                               "1. Imprimir Lista.\n"
                               "2. Agregar Personas.\n"
                               "3. Reclamar Subsidio.\n"
                               "4. Personas Que Retiraron.\n"
                               "5. Total Dinero Entregado.\n"
                               "0. Salir.\n"
                               "-> "))
            if (opcion == 1):
                miLista.mostrarLista()
            
            elif (opcion == 2):
                miBen.agregarBeneficiario(miLista)
            elif (opcion == 3):
                miBen.sacarBeneficiario(miLista)
            elif (opcion == 4):
                miBen.contarPersonas()
            elif (opcion == 5):
                miBen.contarDinero()
            elif (opcion == 0):
                print("Hasta Pronto")
        

    main()