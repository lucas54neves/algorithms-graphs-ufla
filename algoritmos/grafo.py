from vertice import Vertice

class Grafo:
    def __init__(self, n):
        self.quantidade_vertices = n

        # Lista de adjacencia para representar o grafo
        self.lista_adjacencia = []
        for i in range(self.quantidade_vertices):
            self.lista_adjacencia.append([])

        # Matriz de adjacencia para representar o grafo
        self.matriz_adjacencia = []
        for i in range(self.quantidade_vertices):
            linha = []
            for j in range(self.quantidade_vertices):
                linha.append(0)
            self.matriz_adjacencia.append(linha)

        # Lista de vertices para realizar algumas operacoes
        self.lista_vertices = []
        for i in range(self.quantidade_vertices):
            self.lista_vertices.append(Vertice(i))

        # Tempo de visitacao dos vertices
        self.tempo = 0

    def incrementar_tempo(self):
        self.tempo = self.tempo + 1

    def adicionar_aresta_direcional(self, u, v):
        # Adiciona a aresta na lista de adjacencia
        self.lista_adjacencia[u].append(v)

        # Adiciona aresta na matriz de adjacencia
        self.matriz_adjacencia[u][v] = 1

    def adicionar_aresta_nao_direcional(self, u, v):
        # Adiciona a aresta na lista de adjacencia
        self.lista_adjacencia[u].append(v)
        self.lista_adjacencia[v].append(u)

        # Adiciona aresta na matriz de adjacencia
        self.matriz_adjacencia[u][v] = 1
        self.matriz_adjacencia[v][u] = 1

    def get_quantidade_vertices(self):
        return self.quantidade_vertices

    def get_lista_adjacencia(self):
        return self.lista_adjacencia

    def get_matriz_adjacencia(self):
        return self.matriz_adjacencia

    def get_lista_vertices(self):
        return self.lista_vertices

    def get_tempo(self):
        return self.tempo
