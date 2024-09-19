
import sys
lista=[]
print(sys.getsizeof(lista))
def sumar():
    
    while len(lista) <=2:
        i=int(input("Ingrese el numero: "))
        lista.append(i)
    resultado=sum(lista)
    print(resultado)
    print(sys.getsizeof(resultado))
    print(sys.getsizeof(lista))

sumar()
