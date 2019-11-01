# Classe que representa o vertice
class Vertice:
    def __init__(self, indice):
        self.indice = indice
        self.adjacentes = []

    def adicionar_aresta(self, adjacente):
        self.adjacentes.append(adjacente)

# Classe que representa o grafo
class Grafo:
    def __init__(self, n):
        self.tempo = 0
        self.vertices = []
        for i in range(n):
            self.vertices.append(Vertice(i))
        self.quantidade_vertices = n

    def adicionar_aresta(self, u, v):
        self.vertices[u].adjacentes.append(self.vertices[v])
        self.vertices[v].adjacentes.append(self.vertices[u])

    def remover_aresta(self, u, v):
        print("Remover {} - {}".format(u, v))
        for index, key in enumerate(self.vertices[u].adjacentes):
            if key == v:
                self.vertices[u].pop(index)
        for index, key in enumerate(self.vertices[v].adjacentes):
            if key == u:
                sself.vertices[v].pop(index)
        #self.vertices[u].adjacentes.pop(self.vertices[v])
        #self.vertices[v].adjacentes.pop(self.vertices[u])

    # Funcao baseada em DFS que conta os vertices aucansaveis por v
    def contar_alcancaveis(self, v, visitados):
        quantidade = 1
        visitados[v.indice] = True
        for i in v.adjacentes:
            if not visitados[i.indice]:
                quantidade += self.contar_alcancaveis(i, visitados)
        return quantidade

    def aresta_valida(self, u, v):
        if len(self.vertices[u].adjacentes) == 1:
            return True
        else:
            visitados = [False] * (self.quantidade_vertices)
            valor1 = self.contar_alcancaveis(self.vertices[u], visitados)
            self.remover_aresta(u, v)
            visitados = [False] * (self.quantidade_vertices)
            valor2 = self.contar_alcancaveis(self.vertices[u], visitados)
            self.adicionar_aresta(u, v)
            return False if valor1 > valor2 else True

    def caminho_euleriano(self, inicial):
        for adjacente in self.vertices[inicial.indice].adjacentes:
            if self.aresta_valida(inicial.indice, adjacente.indice):
                print("%d-%d " %(inicial.indice, adjacente.indice))
                self.remover_aresta(inicial.indice, adjacente.indice)
                self.caminho_euleriano(adjacente)

    def imprimir_caminho(self):
        u = 0
        for i in range(self.quantidade_vertices):
            if len(self.vertices[i].adjacentes) % 2 != 0:
                u = i
                break
        print("\n")
        self.caminho_euleriano(self.vertices[u])

g1 = Grafo(4)
g1.adicionar_aresta(0, 1)
g1.adicionar_aresta(0, 2)
g1.adicionar_aresta(1, 2)
g1.adicionar_aresta(2, 3)
g1.imprimir_caminho()


g2 = Grafo(3)
g2.adicionar_aresta(0, 1)
g2.adicionar_aresta(1, 2)
g2.adicionar_aresta(2, 0)
g2.imprimir_caminho()

g3 = Grafo (5)
g3.adicionar_aresta(1, 0)
g3.adicionar_aresta(0, 2)
g3.adicionar_aresta(2, 1)
g3.adicionar_aresta(0, 3)
g3.adicionar_aresta(3, 4)
g3.adicionar_aresta(3, 2)
g3.adicionar_aresta(3, 1)
g3.adicionar_aresta(2, 4)
g3.imprimir_caminho()
