import sys

def main():
    vector1=[None] * 4 #2
    vector2=[None] * 4 #2
    vector3=[None] * 4 #2
    print(f"coste de los vectores = {sys.getsizeof(vector1)}")
    
    for i in range(len(vector1)):#2n+2 --> 7n+2
        valor=int(input(f"Ingrese el valor {i+1} para el vector 1: "))#4n
        vector1[i]=valor#1n

    for i in range(len(vector2)):#2n+2-->7n+2
        valor=int(input(f"Ingrese el valor {i+1} para el vector 2: "))#4n
        vector2[i]=valor#1n

    for i in range(len(vector3)):#2n+2 --> 5n+2
        vector3[i]=suma(vector1[i],vector2[i])#2n+1n=3n

    print(f"El coeste del valor = {sys.getsizeof(valor)}")
    print(f"El coeste de los vectores 1 y 2 = {sys.getsizeof(vector1)}")
    print(f"el coste del vector 3= {sys.getsizeof(vector3)}")

    print("El resultado de la suma es: ")#1
    for valor in vector3:#2n+2-->3n+2
        print(valor)#1n
    
def suma(num1, num2):
    return num1+num2#2
    
main()#22n+15 O(n)=n

