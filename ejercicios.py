

lista=[]

def sumar():
    
    while len(lista) <=2:
        i=int(input("Ingrese el numero: "))
        lista.append(i)
    resultado=sum(lista)
    print(resultado)
sumar()
