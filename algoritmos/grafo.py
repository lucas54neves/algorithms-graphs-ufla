from vertice import Vertice

class Grafo:
    def __init__(self, n):
        self.quantidade_vertices = n
        
        # Grafo eh representado como uma lista de adjacencia para realizar a DFS
        self.lista_adjacencia = []
        for i in range(self.quantidade_vertices):
            self.lista_adjacencia.append([])
        
        # Lista de vertices para realizar algumas operacoes
        self.lista_vertices = []
        for i in range(self.quantidade_vertices):
            self.lista_vertices.append(Vertice(i))
        
        # Tempo de visitacao dos vertices
        self.tempo = 0
    
    def incrementar_tempo(self):
        self.tempo = self.tempo + 1
    
    def adicionar_aresta_direcional(self, u, v):
        self.lista_adjacencia[u].append(v)
    
    def adicionar_aresta_nao_direcional(self, u, v):
        self.lista_adjacencia[u].append(v)
        self.lista_adjacencia[v].append(u)
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices
    
    def get_lista_adjacencia(self):
        return self.lista_adjacencia
    
    def get_lista_vertices(self):
        return self.lista_vertices
    
    def get_tempo(self):
        return self.tempo
