


def inicializar(n):
    matriz = []
    valor=1
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(valor)
            valor += 1
        return matriz

    
def obtener_diagrama_principal(matriz):
    n=len(matriz)

    diagramaPrincipal = []


    for i in range(n):
        for j in range(n):
            if i == j:
                diagramaPrincipal.append(matriz[i][j])

    return diagramaPrincipal
    
def obtener_diagonal_secundario(matriz):
    n = len(matriz)

    diagrama_secundario=[]
    for i in range(n):
        for j in range(n):
            if j == (n-1-i):
                diagrama_secundario.append(matriz[i][j])
        return diagrama_secundario

def visualizar_array(array):
    for valor in array:
        print(valor)


matriz=inicializar(5)
print("\nDiagonal principal")
diagramaPrincipal=obtener_diagrama_principal(matriz)
visualizar_array(diagramaPrincipal)
diagonalSec=obtener_diagonal_secundario(matriz)
print("\nDiagonal secundaria")
visualizar_array(diagonalSec)

