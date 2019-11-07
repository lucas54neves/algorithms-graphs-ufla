import math

class Vertice:
    # Construtor do vertice
    # x = coordenada x
    # y = coordenada y
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linha:
    def __init__(self):
        self.estacoes = []

    def adicionar_estacoes(self, vertice):
        self.estacoes.append(vertice)

class Grafo:
    def __init__(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')

        linha = arquivo.readline()
        valores = linha.split()

        casa = Vertice(int(valores[0]), int(valores[1]))
        escola = Vertice(int(valores[2]), int(valores[3]))

        linha = arquivo.readline()

        # Leitura das coordenadas das linhas de metro
        linhas = []
        while linha:
            valores = linha.split()
            linha_metro = Linha()

            while valores:
                coordenada_x = valores.pop(0)
                coordenada_y = valores.pop(0)

                if coordenada_x != -1 and coordenada_y != -1:
                    linha_metro.adicionar_estacoes(Vertice(int(coordenada_x), int(coordenada_y)))

            linhas.append(linha_metro)

            linha = arquivo.readline()

        soma = 0
        for linha in linhas:
            soma += len(linha.estacoes)

        self.n = 2 + soma

        self.matriz = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                linha.append(0)
            self.matriz.append(linha)

        arestas = []
        arestas.append([casa, 0])

        i = 1
        for linha in linhas:
            for estacao in linha.estacoes:
                arestas.append([estacao, i])
            i += 1

        arestas.append([escola, 0])

        i = 0
        for aresta1 in arestas:
            j = 0
            for aresta2 in arestas:
                if aresta1[1] == 0:
                    self.matriz[i][j] = self.calcular_tempo(aresta1[0], aresta2[0], 1.7)
                elif aresta1[1] == aresta2[1]:
                    self.matriz[i][j] = self.calcular_tempo(aresta1[0], aresta2[0], 3.1111111)
                else:
                    self.matriz[i][j] = self.calcular_tempo(aresta1[0], aresta2[0], 1.7)
                j += 1
            i += 1

    def calcular_distancias(self, vertice1, vertice2):
        return math.sqrt(math.pow((vertice1.x - vertice2.x), 2) + math.pow((vertice1.y - vertice2.y), 2))

    def calcular_tempo(self, vertice1, vertice2, velocidade):
        return math.ceil((self.calcular_distancias(vertice1, vertice2) / velocidade) / 60)

    def imprimir_matriz(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])

    def floyd_warshall(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.matriz[i][j] > self.matriz[i][k] + self.matriz[k][j]:
                        self.matriz[i][j] = self.matriz[i][k] + self.matriz[k][j]

def main():
    grafo = Grafo("Ex3.txt")
    grafo.floyd_warshall()
    grafo.imprimir_matriz()

if __name__ == "__main__":
    main()
