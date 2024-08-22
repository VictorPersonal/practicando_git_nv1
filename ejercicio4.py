import sys
try:
    base=float(input("Ingrese la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))

    area=base*altura
    if area > 500:
        print("El triangulo tiene una gran tamaño, el cual es de {}".format(area))
        print("El peso de la base es: ", sys.getsizeof(base),"\n","el peso de la altura es: ", sys.getsizeof(altura),"\n", "el peso del area = ", sys.getsizeof(area))
    else:
        print("El triangulo tiene poco tamaño, el cual es de {}".format(area))
        print("El peso de la base es:", sys.getsizeof(base),"\n","el peso de la altura es:", sys.getsizeof(altura),"\n", "el peso del area =", sys.getsizeof(area))
except TypeError as e:
    print(f"Error: Se intentó realizar una operación con tipos de datos incompatibles. {e}")
except ValueError as error:
    print(f"uno de los valores no es numérico {error}")