import sys
try:
    dia=int(input("Introduzca día de la semana:"))
    print("Memoria usada para el numero que representa el dia es de:", sys.getsizeof(dia))
    if dia == 1:
        mensaje="Lunes"
    elif dia == 2:
        mensaje="Martes"
    elif dia == 3:
        mensaje="Miércoles"
    elif dia == 4:
        mensaje="Jueves"
    elif dia == 5:
        mensaje="Viernes"
    elif dia == 6:
        mensaje="Sábado"
    elif dia == 7:
        mensaje="Domingo"
    else:
        print("ERROR: Día incorrecto.")
    print(mensaje)
    print(f"Memoria usada a la variable que gurada el dia es de: ", sys.getsizeof(mensaje))
except ValueError as error:
    mensaje=f"Error la variable debe ser numérica{error}"
    print("Como hubo excepción dentro del programa el peso del mensaje es de:", sys.getsizeof(mensaje))
