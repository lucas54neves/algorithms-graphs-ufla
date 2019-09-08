from vertice import Vertice

class Grafo:
    def __init__(self, n):
        # Cria a lista de adjacencia
        self.lista_adj = []
        for i in range(n):
            self.lista_adj.append([])
        self.quantidade_vertices = n
        # Cria a lista de vertices
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(Vertice(i))
    
    def get_lista_adj(self):
        return self.lista_adj
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices
    
    def get_lista_vertices(self):
        return self.lista_vertices
