

class Votante():

    def __init__(self, nombre, edad, sexo): #4
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.listaVotantes=[]

    def ingresarAlVotante(self):#20n+3
        for votante in range(4):#2n+2 --> 20n+2
            print(f"Votante {votante+1}")#2n
            nombreVotante=input("Ingrese el nombre del votante: ")#2n
            EdadVotante=int(input("Ingrese la edad del votante: "))#3n
            sexo=input("Ingrese el sexo: (Preferiblemente F --> Femenino; M --> Masculino; O --> Otro): ").upper()#3n
            if sexo == "masculino" or sexo == "femenino" or sexo == "otro":#2n
                inicial_sexo= sexo[0]#1n
                votanteGuardado=Votante(nombreVotante,EdadVotante,sexo)#4n
                self.listaVotantes.append(votanteGuardado)#1n
            else:
                print("Sexo no válido")
        
        return self.listaVotantes#1

    def selectVotantesPorEdad(self):#4n+5
        mayores_a_18_menores_a_20=0#1
        mayores_20_menores_30=0#1
        mayores_30=0#1
        for votante in self.listaVotantes:#2n+2 --> 4n +2
            if 18<= votante.edad <= 20:#1n
                mayores_a_18_menores_a_20+=1 #1n
            elif 20 < votante.edad <= 30:
                mayores_20_menores_30+=1

            else:
                mayores_30+=1
        return mayores_a_18_menores_a_20, mayores_20_menores_30, mayores_30#1
    

    def mostrarResult(self):#4n+8+2=4n+10
        rango_18_20, rango_21_30, rango_30= self.selectVotantesPorEdad()#4n+5+3=4n+8
        print(f"Resultados\na. Votantes entre 18 y 20 años: {rango_18_20}\nb. Votantes entre 21 y 30 años: {rango_21_30}\nc. Votantes mayores de 30 años: {rango_30}") #2





