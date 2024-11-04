from agregarInicio import AgregarInicio
from lista import Lista
from persona import Persona
import random
class Main():

    def main():
        nombres = ["Ana", "Juan", "Luis", "María", "Carlos", "Sofía", "Diego", "Lucía", "Miguel", "Laura"]
        miLista = Lista()

        # Agregar 50 personas a la lista con nombre y edad aleatoria
        for i in range(5):
            AgregarInicio(miLista).AgregarInicioLista(Persona(random.choice(nombres), random.randint(5, 17)))

        # Mostrar la lista
        nodo_actual = miLista.getCabeza()
        while nodo_actual is not None:
            print(f"{nodo_actual.getDato()}", end=" -> \n")
            nodo_actual = nodo_actual.getSiguiente()
        print("None")

Main.main()