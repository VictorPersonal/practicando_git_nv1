class Estudiante():
    def __init__(self, nombre, edad, sexo, nota):#4 --> el metodo constructor no se tiene en cuenta haste que se llame un objeto de la clase
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.nota=nota
    @staticmethod
    def cargarAlEstudiante():#25n+4
        lista=[]#1
        for estudiante in range(2): #2n+2
            print(f"Estudiante ingresado número: {estudiante+1}")#2n
            nombre=input("Ingrese el nombre del estudiante: ").lower()#3n
            edad=int(input("Ingrese la edad del alumno: "))#3n
            sexo=input("Ingrese el sexo o género del alumno: ").lower()#3n
            nota=float(input("Ingrese la nota del alumno: "))#3n

            if sexo == "masculino" or sexo == "femenino" or sexo == "otro":#2n
                inicial_sexo= sexo[0]
                estudianteIngresado=Estudiante(nombre,edad,inicial_sexo,nota)#5n
                lista.append(estudianteIngresado)
            else:
                print("Sexo no válido")
        
        return lista#1

    @staticmethod
    def calcularHombresYMujeresGananAsignatura(lista):#6n+6
        hombresGanan=0#1
        mujeresGanan=0#1
        lista_estudiantes_apropados=[]#1
        for estudiante in lista:#2n+2 --> 6n+2
            if estudiante.nota >= 4.5:#1n
                lista_estudiantes_apropados.append(estudiante.nombre)#1n
                if estudiante.sexo == "m":#1n
                    hombresGanan+=1#1n
                elif estudiante.sexo == "f":
                    mujeresGanan += 1

        return hombresGanan,mujeresGanan, lista_estudiantes_apropados#1

print("Datos de la primera lista:")#1
lista1=Estudiante.cargarAlEstudiante()#25n+4+1=25n+5
print("Datos de la segunda lista")#1
lista2=Estudiante.cargarAlEstudiante()#25n+4+1=25n+5
lista_total= lista1+lista2#2

hombres_aprobados, mujeres_aprobadas, lista_estimulos = Estudiante.calcularHombresYMujeresGananAsignatura(lista_total)#6n+8+3=6n+11

print(f"\nHombres apropados para el estímulo: {hombres_aprobados}")#2
print(f"Mujeres apropados para el estímulo: {mujeres_aprobadas}\n")#2
print(f"\nListado de estudiantes que reciben estimulo académico:")#2
for i in lista_estimulos:#2n+2 -->4n+2
    print(f"- {i}")#2n

#O(n)= 60n+33