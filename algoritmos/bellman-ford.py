# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        self.indice = i
        self.distancia = float('inf')
        self.pai = None

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
        self.vertice1 = u
        self.vertice2 = v
        self.peso = peso

    def get_vertice1(self):
        return self.vertice1

    def get_vertice2(self):
        return self.vertice2

    def get_peso(self):
        return self.peso

# Classe que representa o grafo
class Grafo:
    def __init__(self, n):
        self.quantidade_vertices = n
        self.lista_vertices = []
        for i in range(self.quantidade_vertices):
            self.lista_vertices.append(Vertice(i))
        self.lista_arestas = []

    #def relax(self, u, v, aresta):
    #    if self.lista_vertices[v].get_distancia() > self.lista_vertices[u].get_distancia() + self.lista_arestas[are]

    def retornar_peso(self, u, v):
        indice = self.lista_arestas.index(key=lambda x: x.get_vertice1() == u and x.get_vertice2() == v)
        return self.lista_arestas[indice].get_peso()

    def adicionar_aresta(self, u, v, peso):
        self.lista_arestas.append(Aresta(u, v, peso))

grafo = Grafo(3)
grafo.adicionar_aresta(1,2, 4.5)
print(grafo.retornar_peso(1, 2))
