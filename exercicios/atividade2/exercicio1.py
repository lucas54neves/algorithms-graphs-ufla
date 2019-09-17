# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        # Indice do vertice
        self.indice = i

# Classe que representa o grafo
class Grafo:
    # n eh a quantidade de vertices
    def __init__(self, n):
        # Instancia a lista de adjacencia
        self.lista_adjacencia = []
        for i in range(n):
            self.lista_adjacencia.append([])
        # Define a quantidade de vertices do grafo
        self.quantidade_vertices = n
        # Instancia a lista de vertices
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(Vertice(i))
