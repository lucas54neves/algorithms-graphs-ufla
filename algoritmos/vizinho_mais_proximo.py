import random
import math

# Classe que representa o vertice
class Vertice:
    def __init__(self, indice, x, y, dado):
        self.indice = indice
        self.x = x
        self.y = y
        self.dado = dado
        self.adjacentes = []
        self.visitado = False
        self.distancia = 1000000

    def get_indice(self):
        return self.indice

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_dado(self):
        return self.dado

    def get_adjacentes(self):
        return self.adjacentes

    def get_visitado(self):
        return self.visitado

    def get_distancia(self):
        return self.distancia

    def adicionar_aresta(self, adjacente):
        self.adjacentes.append(adjacente)

    def visitar(self):
        self.visitado = True

    def calcular_distancia(self, vertice):
        xa = float(self.x)
        ya = float(self.y)
        xb = float(vertice.get_x())
        yb = float(vertice.get_y())
        self.distancia = math.sqrt((xa-xb)**2 +(ya-yb)**2)

# Classe que representa o grafo
class Grafo:
    def __init__(self):
        self.vertices = []

    def get_vertices(self):
        return self.vertices

    def quantidade_vertices(self):
        return len(self.vertices)

    def adicionar_vertice(self, x, y, dado):
        self.vertices.append(Vertice(len(self.vertices), x, y, dado))

    # Considerando que o grafo seja nao orientado
    def adicionar_aresta(self, u, v):
        self.vertices[u.get_indice()].get_adjacentes().append(v)
        self.vertices[v.get_indice()].get_adjacentes().append(u)

    def calcular_distancias(self, vertice1):
        for vertice2 in self.vertices:
            vertice2.calcular_distancia(vertice1)

    def todos_visitados(self):
        for vertice in self.vertices:
            if not vertice.get_visitado():
                return False
        return True

    def mais_proximo(self, vertice_atual):
        self.calcular_distancias(vertice_atual)

        proximo = vertice_atual

        for vertice in self.vertices:
            if vertice.get_distancia() < proximo.get_distancia() and not vertice.get_visitado():
                proximo = vertice

        return proximo.get_indice()

    def vizinho_mais_proximo(self):
        vertice_inicial = self.vertices[random.randint(0, (self.quantidade_vertices()-1))]
        vertice_inicial.visitar()
        vertice = vertice_inicial
        mais_proximo = None

        while not self.todos_visitados():
            self.calcular_distancias(vertice)
            mais_proximo = self.mais_proximo(vertice)
            self.adicionar_aresta(vertice, mais_proximo)
            self.imprimir_distancias()

            mais_proximo.visitar()
            vertice_inicial = mais_proximo

        self.adicionar_aresta(vertice_inicial, mais_proximo)

    def imprimir_adjacentes(self):
        for vertice in self.vertices:
            resultado = str(vertice.get_indice()) + ": "
            for adjacente in vertice.get_adjacentes():
                resultado += " -> " + str(adjacente.get_indice())
            print(resultado)

    def imprimir_distancias(self):
        for vertice in self.vertices:
            print("{} {}".format(vertice.get_indice(), vertice.get_distancia()))

grafo = Grafo()
grafo.adicionar_vertice(0,1,2)
grafo.adicionar_vertice(1,2,2)
grafo.adicionar_vertice(2,3,2)
grafo.adicionar_vertice(0,3,2)
grafo.adicionar_vertice(1,4,2)
grafo.adicionar_vertice(2,4,2)
grafo.vizinho_mais_proximo()
grafo.imprimir_adjacentes()
