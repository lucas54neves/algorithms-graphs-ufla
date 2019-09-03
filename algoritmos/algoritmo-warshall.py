# Algoritmo de Warshall para uma matriz quadrada de tamanho n
def warshall (matriz, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = int(matriz[i][j] == 1 or (matriz[i][k] == 1 and matriz[k][j] == 1))

A = []
for i in range(6):
    A.append( [0] * 6 )
A[0][1] = 1
A[1][4] = 1
A[0][4] = 1
A[2][5] = 1
A[4][2] = 1
A[3][0] = 1
for i in range(6):
    print(A[i])
print("==========")

warshall(A, 6)
for i in range(6):
    print(A[i])