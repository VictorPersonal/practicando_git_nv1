import random

# Clase Persona que representa a un beneficiario
class Persona:
    def __init__(self, edad):
        self.edad = edad
        self.subsidio = self.calcular_subsidio()

    def calcular_subsidio(self):
        if 5 <= self.edad <= 9:
            return 60000
        elif 10 <= self.edad <= 13:
            return 80000
        elif 14 <= self.edad <= 17:
            return 100000
        return 0

# Nodo de la lista enlazada
class Nodo:
    def __init__(self, persona):
        self.persona = persona
        self.siguiente = None

# Clase Cola que maneja los nodos de manera FIFO
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.total_personas = 0
        self.total_dinero = 0

    # Método para agregar personas a la cola
    def encolar(self, persona):
        nuevo_nodo = Nodo(persona)
        if not self.frente:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.total_personas += 1
        self.total_dinero += persona.subsidio

    # Método para simular el reclamo del subsidio y eliminar el nodo del frente
    def desencolar(self):
        if not self.frente:
            print("La cola está vacía.")
            return None
        persona_atendida = self.frente.persona
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        self.total_personas -= 1
        self.total_dinero -= persona_atendida.subsidio
        return persona_atendida

    # Método para mostrar la cola actual
    def mostrar_cola(self):
        actual = self.frente
        while actual:
            print(f"Edad: {actual.persona.edad}, Subsidio: {actual.persona.subsidio}")
            actual = actual.siguiente

    # Método para mostrar el total de personas y dinero entregado
    def resumen(self):
        print(f"Total de personas atendidas: {50 - self.total_personas}")
        print(f"Total de dinero entregado: {self.total_dinero}")

# Inicializar la cola y añadir personas
cola_beneficiarios = Cola()
for _ in range(5):
    edad_aleatoria = random.randint(5, 17)
    cola_beneficiarios.encolar(Persona(edad_aleatoria))

# Mostrar la lista inicial
print("Lista inicial de beneficiarios:")
cola_beneficiarios.mostrar_cola()

# Simular el reclamo del subsidio
print("\nSimulando el reclamo del subsidio...")
while cola_beneficiarios.frente:
    cola_beneficiarios.desencolar()

# Mostrar el estado final de la cola y el resumen
print("\nCola al finalizar el día:")
cola_beneficiarios.mostrar_cola()
cola_beneficiarios.resumen()
