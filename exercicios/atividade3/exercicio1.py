class Par:
    def __init__(self, i):
        self.id = i
        self.visitada = False

class Grafo:
    def __init__(self, n):
        self.lista_adjacencia = []
        for i in range(n):
            self.lista_adjacencia.append([])

    def adicionar_aresta(self, u, v):
        self.lista_adjacencia[u].append(Par(v))

    def hierholzer(self):
        if len(self.lista_adjacencia) != 0:
            graus = []
            for i in range(len(self.lista_adjacencia)):
                graus.append(len(self.lista_adjacencia[i]))

            caminho_atual = []
            circuito_euleriano = []

            caminho_atual.append(0)
            vertice_atual = 0

            while len(caminho_atual) != 0:
                if (graus[vertice_atual] != 0):
                    caminho_atual.append(vertice_atual)
                    proximo_vertice = self.lista_adjacencia[vertice_atual].pop()
                    graus[vertice_atual] -= 1
                    vertice_atual = proximo_vertice
                else:
                    circuito_euleriano.append(vertice_atual)
                    vertice_atual = caminho_atual.pop()

            retorno = ""
            i = len(circuito_euleriano) - 1
            while i >= 0:
                retorno += " " + str(circuito_euleriano[i])
                i -= 1

            print(retorno)

grafo = Grafo(7)

grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(1, 6)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(2, 4)
grafo.adicionar_aresta(2, 5)
grafo.adicionar_aresta(2, 6)
grafo.adicionar_aresta(4, 5)

grafo.hierholzer()
