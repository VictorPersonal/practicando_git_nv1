class Burbuja():
    def __init__(self):
        pass
    def metodoOrdenarLista(self, listaDesordenada):
        bandera = False #Cuando no haya intercambios se cambia a True
        for i in range(len(listaDesordenada)-1):
            bandera= True
            for j in range(len(listaDesordenada)-1-i):
                if(listaDesordenada[j] > listaDesordenada[j+1]):#Aqui se define el criterio de ordenamiento < DES o > ASC
                    aux=listaDesordenada[j]
                    listaDesordenada[j] = listaDesordenada[j+1]
                    listaDesordenada[j+1]= aux
                    bandera=False

            if(bandera==True):
                break
            texto=""
            for x in listaDesordenada:
                texto=texto + "->" + str(x)
            print("En burbuja La lista en la pasada" + " " + str(i) + "es: "+ " " + texto)
        return listaDesordenada #Aunque ya esta ordenada
