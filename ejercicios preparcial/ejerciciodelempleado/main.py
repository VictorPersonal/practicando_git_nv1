from empleado import Empleado

def main():
    nombre=input("Ingrese el nombre del empleado: ")#2
    cedula=input("Ingrese la cédula del empleado: ")#2
    edad=int(input("Ingrese la edad: "))#3
    salario=int(input("Ingrese el salario: "))#3
    empleadoGuardado=Empleado(nombre, cedula, edad,salario)#5

    salud=empleadoGuardado.getSalario() * 0.125#3
    pension=empleadoGuardado.getSalario() * 0.16#3
    riesgo=empleadoGuardado.getSalario() * 0.35#3
    print(f"Deberá pagar por salud: {salud}")#2
    print(f"Deberá pagar por pensión: {pension}")#2
    print(f"Deberá pagar por riesgos profesionales ARL: {riesgo}")#2


main()#O(n)= 30 S(n) = 265 bytes
