from vertice import Vertice

class Grafo:
    def __init__(self, n):
        # Quantidade de vertices
        self.quantidade_vertices = n

        # Lista de adjacencia
        self.lista_adj = []
        for i in range(n):
            self.lista_adj.append([0] * n)
        
        # Matriz de adjacencia
        self.matriz_adj = []
        for i in range(n):
            self.matriz_adj.append([])
        
        # Lista de vertices para realizar as operacoes
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(Vertice(i))
    
    # Retorna a lista de adjacencia
    def get_lista_adj(self):
        return self.lista_adj
    
    # Retorna a quantidade vertices
    def get_quantidade_vertices(self):
        return self.quantidade_vertices
    
    # Retorna a lista de vertices
    def get_lista_vertices(self):
        return self.lista_vertices

    # Retorna a matriz de adjacencia
    def get_matriz_adj(self):
        return self.matriz_adj

    # Adiciona aresta direcional
    def adicionar_aresta_direcional(self, u, v):
        
    # Adiciona aresta nao direcinal
    def adicionar_aresta_direcional(self, u, v):
        
