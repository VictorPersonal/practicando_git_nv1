
import sys

try:
    edad = int(input("Ingrese la edad: "))
    print(f"Memoria utilizada por 'edad': {sys.getsizeof(edad)} bytes")
    
    if edad < 10:
        mensaje = "De acuerdo con la edad ingresada se puede decir que la persona está en la etapa de la infancia."
    elif 10 <= edad <= 25:
        mensaje = "De acuerdo con la edad ingresada se puede decir que la persona está en la etapa de la adolescencia."
    else:
        mensaje = "De acuerdo con la edad ingresada se puede decir que la persona está en la etapa de la adultez."
    
    print(mensaje)
    print(f"Memoria utilizada por 'mensaje': {sys.getsizeof(mensaje)} bytes")

except ValueError as error:
    mensaje_error = f"El valor ingresado no es numérico. {error}"
    print(mensaje_error)
    print(f"Memoria utilizada por 'mensaje_error': {sys.getsizeof(mensaje_error)} bytes")
