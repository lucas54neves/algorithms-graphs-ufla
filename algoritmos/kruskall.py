from collections import defaultdict

# Classe para representar o grafo
class Grafo:
    def __init__(self, n):
        # Quantidade n de vertices
        self.quantidade_vertices = n

        # Lista para armazenas as arestas
        self.arestas = []

    # Para adicionar a aresta ao grafo
    # Posicao 0 eh o vertice i
    # Posicao 1 eh o vertice j
    # Posicao 2 eh o peso
    def adicionar_aresta(self, vertice_i, vertice_j, peso):
        self.arestas.append(vertice_i, vertice_j, peso)
