
import sys
b=int(input("Ingrese el número que se tomará como base: "))
e=int(input("Ingrese el número que se tomará como exponente: "))
resultado=pow(b,e)
print(sys.getsizeof(b))
print(sys.getsizeof(e))
print(sys.getsizeof(resultado))
print(resultado)