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

        linhas = []
        while linha:
            valores = linha.split()
            linha_metro = Linha()

            i = 0
            while len(valores) > i:
                if valores[i] != -1:
                    linha_metro.adicionar_estacoes(Vertice(int(valores[i]), int(valores[i+1])))
                i += 2

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

        # vertices = {}
        #
        # vertices[0] = casa
        #
        # i = 1
        # for linha in linhas:
        #     for estacao in linha:
        #         vertices[i] = estacao
        #         i += 1
        #
        # vertices[i+1] = escola

        # vertices => posicao eh chave e vertice eh valor
        # dicionario.get(chave) = retorna valor
        # for chave in dicionario:
        # for valor in dicionario.values():

        i = 1
        for linha in linhas:
            for estacao in linha.estacoes:
                self.matriz[1][i] = self.calcular_tempo(casa, estacao, 1.7)
                i += 1
        self.matriz[1][self.n-1] = self.calcular_tempo(casa, escola, 1.7)

        i = 1
        for linha in linhas:
            j = i
            for estacao1 in linha.estacoes:
                self.matriz[i][0] = self.calcular_tempo(estacao1, casa, 1.7)
                for estacao2 in linha.estacoes:
                    if i < self.n and j < self.n:
                        self.matriz[i][j] = self.calcular_tempo(estacao1, estacao2, 3.1111111)
                    j += 1
                self.matriz[i][self.n-1] = self.calcular_tempo(estacao1, escola, 1.7)
                i += 1


        # Indice da linha1
        i = 1
        for linha1 in linhas:
            for estacao1 in linha1.estacoes:
                k = 1
                for linha2 in linhas:
                    for estacao2 in linha1.estacoes:
                        self.matriz[i][k] = self.calcular_tempo(estacao1, estacao2, 1.7)
                        k += 1
                i += 1

    def calcular_distancias(self, vertice1, vertice2):
        return math.sqrt(math.pow((vertice1.x - vertice2.x), 2) + math.pow((vertice1.y - vertice2.y), 2))

    def calcular_tempo(self, vertice1, vertice2, velocidade):
        return math.ceil(self.calcular_distancias(vertice1, vertice2) / velocidade)

    def imprimir_matriz(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])

def main():
    grafo = Grafo("Ex3.txt")
    grafo.imprimir_matriz()

if __name__ == "__main__":
    main()
