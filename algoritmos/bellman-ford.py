# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        self.indice = i
        self.distancia = float('inf')
        self.pai = None

    def get_indice(self):
        return self.indice

    def get_distancia(self):
        return self.distancia

    def get_pai(self):
        return self.pai

    def set_distancia(self, nova_distancia):
        self.distancia = nova_distancia

    def set_pai(self, novo_pai):
        self.pai = novo_pai

# Classe que representa a aresta
class Aresta:
    def __init__(self, u, v, peso):
        self.origem = u
        self.destino = v
        self.peso = peso

    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino

    def get_peso(self):
        return self.peso

# Classe que representa o grafo
class Grafo:
    def __init__(self, n):
        self.quantidade_vertices = n
        self.lista_vertices = []
        for i in range(self.quantidade_vertices):
            self.lista_vertices.append(Vertice(i))
        self.lista_adjacencia = []
        for i in range(self.quantidade_vertices):
            self.lista_adjacencia.append([])

    def relax(self, u, v):
        if self.lista_vertices[v].get_distancia() > self.lista_vertices[u].get_distancia() + self.retornar_peso(u, v):
            self.lista_vertices[v].set_distancia(self.lista_vertices[u].get_distancia() + self.retornar_peso(u, v))
            self.alterar_pai(v, u)

    def retornar_peso(self, u, v):
        for adjacente in self.lista_adjacencia[u]:
            if adjacente.get_destino() == v:
                return adjacente.get_peso()

    def alterar_distancia(self, u, v):
        self.lista_vertices[v].set_distancia(self.lista_vertices[u].get_distancia() + self.retornar_peso(u, v))

    def alterar_pai(self, u, novo_pai):
        self.lista_vertices[u].set_pai(novo_pai)

    def adicionar_aresta(self, u, v, peso):
        self.lista_adjacencia[u].append(Aresta(u, v, peso))

    def bellman_ford(self):
        self.lista_vertices[0].set_distancia(0)
        for i in range(self.quantidade_vertices - 1):
            for aresta in self.lista_adjacencia[i]:
                self.relax(aresta.get_origem(), aresta.get_destino())
        for aresta in self.lista_adjacencia[i]:
            if self.lista_vertices[aresta.get_destino()].get_distancia() > self.lista_vertices[aresta.get_origem()].get_distancia() + self.retornar_peso(aresta.get_origem(), aresta.get_destino()):
                return False
        return True

    def imprimir_resultado(self):
        for i in self.lista_vertices:
            print("{}: {}".format(i.get_indice(), i.get_distancia()))

grafo = Grafo(5)
grafo.adicionar_aresta(0,1,6)
grafo.adicionar_aresta(0,2,7)
grafo.adicionar_aresta(1,2,8)
grafo.adicionar_aresta(1,3,5)
grafo.adicionar_aresta(1,4,-4)
grafo.adicionar_aresta(2,3,-3)
grafo.adicionar_aresta(2,4,9)
grafo.adicionar_aresta(3,2,-2)
grafo.adicionar_aresta(4,0,2)
grafo.adicionar_aresta(4,3,7)
print(grafo.bellman_ford())
grafo.imprimir_resultado()
