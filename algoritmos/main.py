from insercion import Insercion
from seleccion import Seleccion
from burbuja import Burbuja
def imprimirLista(listaOrdenada):
    texto=""
    for x in listaOrdenada:
        texto=texto + "->" + str(x)
    print("La lista ordenada es"  + texto)

class Main():
    def main():
        
        listaDesordenada=[]
        listaOrdenada=[]
        tamaño=int(input("Ingrese el tamaño de la lista: "))
        for i in range(tamaño):
            listaDesordenada.append(int(input("Ingrese el elemento "+ str(i+1)+": ")))
        
        miBurbu=Burbuja()
        listaOrdenada=miBurbu.metodoOrdenarLista(listaDesordenada)
        imprimirLista(listaOrdenada)
        miSelect=Seleccion()
        listaOrdenada= miSelect.ordenarLista(listaDesordenada)
        imprimirLista(listaOrdenada)
        miInsert=Insercion()
        listaOrdenada=miInsert.ordenarLista(listaDesordenada)
        imprimirLista(listaOrdenada)
        

    main()