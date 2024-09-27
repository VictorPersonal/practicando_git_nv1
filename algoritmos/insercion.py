class Insercion():
    def __init__(self):
        pass
    def ordenarLista(self,listaDesordenada):
        for i in range(1, len(listaDesordenada)):#Define las pasadas. ademas garantiza de que la lista quede ordenada
            j=i
            aux=listaDesordenada[i]
            while(j > 0 and aux < listaDesordenada[j-1]):#Realiza las comparaciones hacia atras desde la posicion i, desde la pasada donde estemos.
                listaDesordenada[j] = listaDesordenada[j-1]
                j -= 1 #j =j - 1

            listaDesordenada[j] = aux #Realizo el intercambio
            texto=""
            for x in listaDesordenada:
                texto=texto + "->" + str(x)
            print("En insercion La lista en la pasada" + " " + str(i) + "es: " + texto)
        return listaDesordenada #Aunque ya esta ordenada