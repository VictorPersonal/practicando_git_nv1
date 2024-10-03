from empleado import Empleado
import sys
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
    print(f"Coste de la variable salud= {sys.getsizeof(salud)}")
    print(f"Coste de la variable pensión= {sys.getsizeof(pension)}")
    print(f"Coste de la variable riesgo= {sys.getsizeof(riesgo)}")
    print(f"Coste de la variable objeto empleadoGuardado= {sys.getsizeof(empleadoGuardado)}")
    print(f"Coste de la variable nombre= {sys.getsizeof(empleadoGuardado.nombre)}")
    print(f"Coste de la variable cédula= {sys.getsizeof(empleadoGuardado.getCedula())}")
    print(f"Coste de la variable edad= {sys.getsizeof(empleadoGuardado.edad)}")
    print(f"Coste de la variable salario= {sys.getsizeof(empleadoGuardado.getSalario())}")

main()