class Grafo:
    def __init__(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')

        linha = arquivo.readline()
        self.n = int(linha)

        self.matriz = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                linha.append(0)
            self.matriz.append(linha)

        linha = arquivo.readline()

        while linha:
            valores = linha.split()
            self.adicionar_aresta(int(valores[0]), int(valores[1]))
            linha = arquivo.readline()

    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = 1

    def floyd_warshall(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.matriz[i][k] != 0 and self.matriz[k][j] != 0:
                        self.matriz[i][j] += 1
#int(grafo.get_matriz_adjacencia()[i][j] == 1
#or (grafo.get_matriz_adjacencia()[i][k] == 1
#and grafo.get_matriz_adjacencia()[k][j] == 1))

    def imprimir_matriz(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])

def main():
    grafo = Grafo("Ex4.txt")
    grafo.floyd_warshall()
    grafo.imprimir_matriz()

if __name__ == "__main__":
    main()
