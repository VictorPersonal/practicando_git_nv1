import sys
numeros = []
print("El peso de la lista la cual está vacia es de: ",sys.getsizeof(numeros))

for i in range(3):
    try:
        numero = int(input(f"Ingrese el número entero {i + 1}: "))
        numeros.append(numero)
        numero_mayor = max(numeros)
    except ValueError as error:
        print(f"Error: Debe ingresar un número entero.{error}")
        


print(f"El número mayor de los tres ingresados es: {numero_mayor}")
print("El peso de la variable que almacena al número es: ",sys.getsizeof(numero))
print("El peso de la variable que almacena al número mayor es: ",sys.getsizeof(numero_mayor))
