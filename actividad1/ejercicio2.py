import sys
base=int(input("Ingrese el numero que se tomara como base: "))
exponete=int(input("Ingrese el numero que se tomara como exponente: "))
resultado=pow(base,exponete)
print(sys.getsizeof(base))
print(sys.getsizeof(exponete))
print(resultado)
print(sys.getsizeof(resultado))