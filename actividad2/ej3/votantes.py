

class Votante():

    def __init__(self, nombre, edad, sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.listaVotantes=[]

    def ingresarAlVotante(self):
        for votante in range(4):
            print(f"Votante {votante+1}")
            nombreVotante=input("Ingrese el nombre del votante: ")
            EdadVotante=int(input("Ingrese la edad del votante: "))
            sexo=input("Ingrese el sexo: (Preferiblemente F --> Femenino; M --> Masculino; O --> Otro): ")
            if sexo in ["F","M","O"]:
                return sexo
            print("No se admite el sexo")
            votanteGuardado=Votante(nombreVotante,EdadVotante,sexo)
            self.listaVotantes.append(votanteGuardado)
            return self.listaVotantes

    def selectVotantesPorEdad(self):
        mayores_a_18_menores_a_20=0
        mayores_20_menores_30=0
        mayores_30=0
        for votante in self.listaVotantes:
            if 18<= votante.edad <= 20:
                mayores_a_18_menores_a_20+=1
            elif 20 < votante.edad <= 30:
                mayores_20_menores_30+=1

            else:
                mayores_30+=1
        return mayores_a_18_menores_a_20, mayores_20_menores_30, mayores_30
    

    def mostrarResult(self):
        rango_18_20, rango_21_30, rango_30= self.selectVotantesPorEdad(self.listaVotantes)
        print(f"Resultados\na. Votantes entre 18 y 20 años: {rango_18_20}\nb. Votantes entre 21 y 30 años: {rango_21_30}\nc. Votantes mayores de 30 años: {rango_30}")






        