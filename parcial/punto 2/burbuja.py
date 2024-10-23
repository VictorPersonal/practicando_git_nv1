
def ordenarlista(self, listaDesordenada):
    bandera =False #1
    for i in range(len(listaDesordenada)-1): #2n
        bandera =True #1(n-1) = n-1

        for j in range(len(listaDesordenada)-1-i):#2n(n-1) = 2n^2-2n
            if(listaDesordenada[j] > listaDesordenada[j+1]): 
                aux = 0 #1(n-1)(n-1)=n^2-2n+1
                bandera = False#1(n-1)(n-1)=n^2-2n+1
                aux = listaDesordenada[j]#1(n-1)(n-1)=n^2-2n+1
                listaDesordenada[j] = listaDesordenada[j+1]#2(n-1)(n-1)=2n^2-4n+2
                listaDesordenada[j+1] = aux#2(n-1)(n-1)=2n^2-4n+2
            if (bandera == True): #1(n-1)=n-1
                break
            texto = ""#1(n-1)=n-1
            for k in listaDesordenada:#(2n+2)(n-1)=2n^2-2
                texto = texto +" -> "+ str(k)   #3n^2-3n
            print("La lista en la pasada "+ str(i) +" es: "+texto)#3(n-1)=3n-3
        return listaDesordenada#1
#T(n)= 16n^2-15n+3
#O(n)=n^2