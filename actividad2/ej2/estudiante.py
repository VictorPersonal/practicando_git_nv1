class Estudiante():
    def __init__(self, nombre, edad, sexo, nota):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.nota=nota
    @staticmethod
    def cargarAlEstudiante():
        lista=[]
        for estudiante in range(2):
            print(f"Estudiante ingresado número: {estudiante+1}")
            nombre=input("Ingrese el nombre del estudiante: ").lower()
            edad=int(input("Ingrese la edad del alumno: "))
            sexo=input("Ingrese el sexo o género del alumno: ").lower()
            nota=float(input("Ingrese la nota del alumno: "))

            if sexo == "masculino" or sexo == "femenino" or sexo == "otro":
                inicial_sexo= sexo[0]
                estudianteIngresado=Estudiante(nombre,edad,inicial_sexo,nota)
                lista.append(estudianteIngresado)
            else:
                print("Sexo no válido")
        
        return lista

    @staticmethod
    def calcularHombresYMujeresGananAsignatura(lista):
        hombresGanan=0
        mujeresGanan=0
        lista_estudiantes_apropados=[]
        for estudiante in lista:
            if estudiante.nota >= 4.5:
                lista_estudiantes_apropados.append(estudiante.nombre)
                if estudiante.sexo == "m":
                    hombresGanan+=1
                elif estudiante.sexo == "f":
                    mujeresGanan += 1

        return hombresGanan,mujeresGanan, lista_estudiantes_apropados        

print("Datos de la primera lista:")
lista1=Estudiante.cargarAlEstudiante()
print("Datos de la segunda lista")
lista2=Estudiante.cargarAlEstudiante()
lista_total= lista1+lista2

hombres_aprobados, mujeres_aprobadas, lista_estimulos = Estudiante.calcularHombresYMujeresGananAsignatura(lista_total)

print(f"\nHombres apropados para el estímulo: {hombres_aprobados}")
print(f"Mujeres apropados para el estímulo: {mujeres_aprobadas}\n")
print(f"\nListado de estudiantes que reciben estimulo académico:")
for i in lista_estimulos:
    print(f"- {i}")