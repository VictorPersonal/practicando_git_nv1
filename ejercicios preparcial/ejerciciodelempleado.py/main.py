from empleado import Empleado

def main():
    nombre=input("Ingrese el nombre del empleado: ")
    cedula=input("Ingrese la cédula del empleado: ")
    edad=int(input("Ingrese la edad"))
    salario=int(input("Ingrese el salario: "))
    empleadoGuardado=Empleado(nombre, cedula, edad,salario)

    salud=empleadoGuardado.getSalario() * 0.125
    pension=empleadoGuardado.getSalario() * 0.16
    riesgo=empleadoGuardado.getSalario() * 0.35
    print(f"Deberá pagar por salud: {salud}")
    print(f"Deberá pagar por pensión: {pension}")
    print(f"Deberá pagar por riesgos profesionales ARL: {riesgo}")
