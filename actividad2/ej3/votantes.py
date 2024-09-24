

class Votante():

    def __init__(self, nombre, edad, sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    @staticmethod
    def ingresarAlVotante():
        lista=[]
        for votante in range(4):
            print(f"Votante {votante+1}")
            nombreVotante=input("Ingrese el nombre del votante: ")
            EdadVotante=int(input("Ingrese la edad del votante: "))
            sexo=input("Ingrese el sexo: (Preferiblemente F --> Femenino; M --> Masculino; O --> Otro): ")
            votanteGuardado=Votante(nombreVotante,EdadVotante,sexo)
            lista.append(votanteGuardado)

        return lista
            
            
    @staticmethod
    def selectVotantesPorEdad(lista):
        mayores_a_18_menores_a_20=0
        mayores_20_menores_30=0
        mayores_30=0
        for votante in lista:
            if 18<= votante.edad <= 20:
                mayores_a_18_menores_a_20+=1
            elif 20 < votante.edad <= 30:
                mayores_20_menores_30+=1

            else:
                mayores_30+=1
        return mayores_a_18_menores_a_20, mayores_20_menores_30, mayores_30


print("Cargando lista....")
lista_votantes=Votante.ingresarAlVotante()

rango_18_20, rango_21_30, rango_30= Votante.selectVotantesPorEdad(lista_votantes)
print(f"Resultados\na. Votantes entre 18 y 20 años: {rango_18_20}\nb. Votantes entre 21 y 30 años: {rango_21_30}\nc. Votantes mayores de 30 años: {rango_30}")






        