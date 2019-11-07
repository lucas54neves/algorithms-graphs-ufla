import math

class Vertice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tempo = float("inf")
        self.pai = None
        self.arestas = []

    def relax(self, aresta):
        self.tempo = aresta.adjacente.tempo + aresta.peso
        self.pai = adjacente

    def adicionar_aresta(self, destino, peso):
        self.arestas.append(Aresta(destino, peso))

class Aresta:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

class Linha:
    def __init__(self):
        self.estacoes = []

    def adicionar_estacoes(self, vertice):
        self.estacoes.append(vertice)

class Grafo:
    def __init__(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        self.vertices = []

        linha = arquivo.readline()
        valores = linha.split()

        self.vertices.append([Vertice(int(valores[0]), int(valores[1])), 0])
        self.vertices.append([Vertice(int(valores[2]), int(valores[3])), 0])

        linha = arquivo.readline()

        # Leitura das coordenadas das linhas de metro
        i = 1
        while linha:
            valores = linha.split()
            linha_metro = Linha()

            while valores:
                coordenada_x = int(valores.pop(0))
                coordenada_y = int(valores.pop(0))

                if coordenada_x != -1 and coordenada_y != -1:
                    self.vertices.append([Vertice(coordenada_x, coordenada_y), i])

            i += 1
            linha = arquivo.readline()

        i = 0
        for vertice1 in self.vertices:
            j = 0
            for vertice2 in self.vertices:
                if vertice1[1] == 0:
                    vertice1[0].adicionar_aresta(vertice2, self.calcular_tempo(vertice1[0], vertice2[0], 1.7))
                elif vertice1[1] == vertice2[1]:
                    vertice1[0].adicionar_aresta(vertice2, self.calcular_tempo(vertice1[0], vertice2[0], 3.1111111111))
                else:
                    vertice1[0].adicionar_aresta(vertice2, self.calcular_tempo(vertice1[0], vertice2[0], 1.7))
                j += 1
            i += 1

    def calcular_distancias(self, vertice1, vertice2):
        return math.sqrt(math.pow((vertice1.x - vertice2.x), 2) + math.pow((vertice1.y - vertice2.y), 2))

    def calcular_tempo(self, vertice1, vertice2, velocidade):
        return math.ceil((self.calcular_distancias(vertice1, vertice2) / velocidade) / 60)

    def imprimir_resultado(self):
        print(self.vertices[len(self.vertices) - 1].tempo)

    def dijkstra(self):
        self.inicializar_vertices()
        
        self.vertices[0][0].tempo = 0

        conjunto_q = self.vertices
        
        while len(conjunto_q) != 0:
            u = min(conjunto_q, key=lambda v: v[0].tempo)
            for aresta in u[0].arestas:
                if u[0].tempo > aresta.destino[0].tempo + aresta.peso:
                    u[0].relax(aresta)

    def inicializar_vertices(self):
        for vertice in self.vertices:
            vertice[0].tempo = float("inf")
            vertice[0].pai = None

def main():
    grafo = Grafo("Ex3.txt")
    grafo.dijkstra()
    grafo.imprimir_resultado()

if __name__ == "__main__":
    main()
