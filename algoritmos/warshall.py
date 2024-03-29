from grafo import *

# Algoritmo de Warshall usando a matriz de adjacencia de um grafo
def warshall (grafo):
    for k in range(grafo.get_quantidade_vertices()):
        for i in range(grafo.get_quantidade_vertices()):
            for j in range(grafo.get_quantidade_vertices()):
                grafo.get_matriz_adjacencia()[i][j] = int(grafo.get_matriz_adjacencia()[i][j] == 1 or (grafo.get_matriz_adjacencia()[i][k] == 1 and grafo.get_matriz_adjacencia()[k][j] == 1))
