
import sys

def inicializar(n):
    matriz = []
    valor=1
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(valor)
            valor += 1
        return matriz
    print(f"El coste de la matriz es de: {sys.getsizeof(matriz)}")
    print(f"El coste del valor es de: {sys.getsizeof(valor)}")
    
def obtener_diagrama_principal(matriz):
    n=len(matriz)
    print(f"El valor de n dentro de la función 'obtener_diagrama_principal es de: {sys.getsizeof(n)}'")
    diagramaPrincipal = []
    print(f"El valor de la lista 'diagramaPrincipal' dentro de la función 'obtener_diagrama_principal es de: {sys.getsizeof(diagramaPrincipal)}'")

    for i in range(n):
        for j in range(n):
            if i == j:
                diagramaPrincipal.append(matriz[i][j])
    print(f"El coste espacial de la lista diagramaPrincipal es de {sys.getsizeof(diagramaPrincipal)}")
    return diagramaPrincipal
    
def obtener_diagonal_secundario(matriz):
    n = len(matriz)
    print(f"El valor de la variable n: {sys.getsizeof(n)}")
    diagrama_secundario=[]
    for i in range(n):
        for j in range(n):
            if j == (n-1-i):
                diagrama_secundario.append(matriz[i][j])
        return diagrama_secundario
    print(f"Coste de la lista diagrama secundario: {sys.getsizeof(diagrama_secundario)}")
def visualizar_array(array):
    for valor in array:
        print(valor)
    print(f"el coste del valor: {sys.getsizeof(valor)}")

matriz=inicializar(5)
print("\nDiagonal principal")
diagramaPrincipal=obtener_diagrama_principal(matriz)
visualizar_array(diagramaPrincipal)
diagonalSec=obtener_diagonal_secundario(matriz)
print("\nDiagonal secundaria")
visualizar_array(diagonalSec)

