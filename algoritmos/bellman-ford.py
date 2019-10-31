# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        self.indice = i
        self.distancia = float('inf')
        self.pai = None
        self.adjacentes = []

# Classe que representa o grafo
class Grafo:
    def __init__(self, n):
        self.vertices = []
        for i in range(n):
            self.vertices.append(Vertice(i))
        self.arestas = []
        self.quantidade_vertices = n

    def adicionar_aresta(self, u, v, w):
        self.arestas.append([u, v, w])

    def bellman_ford(self, inicial):
        self.vertices[inicial].distancia = 0
        for i in range(self.quantidade_vertices - 1):
            for aresta in self.arestas:
                u = aresta[0]
                v = aresta[1]
                w = aresta[2]
                if (self.vertices[v].distancia > self.vertices[u].distancia + w):
                    self.vertices[v].distancia = self.vertices[u].distancia + w
                    self.vertices[v].pai = self.vertices[u]

        for aresta in self.arestas:
            u = aresta[0]
            v = aresta[1]
            w = aresta[2]
            if (self.vertices[v].distancia > self.vertices[u].distancia + w):
                # Se existe um ciclo de peso negativo, eh atribuido menos infinito
                # para a distancia do vertice
                self.vertices[v].distancia = -float("inf")

    def imprimir_resultado(self):
        for i in self.vertices  :
            print("Vertice {} - Distancia {}".format(i.indice, i.distancia))

# Grafo sem ciclo com peso negativo
grafo1 = Grafo(6)
grafo1.adicionar_aresta(0,1,8)
grafo1.adicionar_aresta(0,2,10)
grafo1.adicionar_aresta(1,3,1)
grafo1.adicionar_aresta(2,5,2)
grafo1.adicionar_aresta(3,2,-4)
grafo1.adicionar_aresta(3,5,-1)
grafo1.adicionar_aresta(4,2,1)
grafo1.adicionar_aresta(5,4,-2)
grafo1.bellman_ford(0)
print("Grafo 1")
grafo1.imprimir_resultado()

# Grafo com ciclo com peso negativo
grafo2 = Grafo(6)
grafo2.adicionar_aresta(0,1,8)
grafo2.adicionar_aresta(0,2,10)
grafo2.adicionar_aresta(1,3,1)
grafo2.adicionar_aresta(2,5,2)
grafo2.adicionar_aresta(3,2,-4)
grafo2.adicionar_aresta(5,3,-1)
grafo2.adicionar_aresta(4,2,1)
grafo2.adicionar_aresta(5,4,-2)
grafo2.bellman_ford(0)
print("Grafo 2")
grafo2.imprimir_resultado()
