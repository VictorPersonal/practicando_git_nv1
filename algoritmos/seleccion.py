class Seleccion():
    def __init__(self):
        pass
    def ordenarLista(self, listaDesordenada):
        for i in range(len(listaDesordenada)-1):
            indiceMenor=i#1(n-1)
            for j in range(i+1,len(listaDesordenada)):#2n(n-1)  #Bucle que realiza las comparaciones buscando el elemento menor
                if (listaDesordenada[j] < listaDesordenada[indiceMenor]):#1(n-1)(n-1) #Aqui se define el criterio de ordenamiento < ASC o > DES
                    #SI EL DEL LADO DERECHO ES MENOR AL DEL LADO IZQUIERDO
                    indiceMenor = j #1(n-1)(n-1)
            if (i != indiceMenor):# 1(n-1) Aqui se realiza el intercambio si el el menor no esta en la posicion correcta
                aux=listaDesordenada[i]#1(n-1)
                listaDesordenada[i] = listaDesordenada[indiceMenor]#1(n-1)
                listaDesordenada[indiceMenor] = aux#1(n-1)
            texto=""#1(n-1)
            for x in listaDesordenada:#2n+2(n-1)=2n^2-2n+2n-2=2n^2-2
                texto=texto + "->" + str(x)#3(n)(n-1)=3n(n-1)=3n^2-3n
            print("En seleccion La lista en la pasada" + " "+ str(i) + "es: " + texto)#3(n-1)=3n-3
        return listaDesordenada #Aunque ya esta ordenada