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
                        if self.matriz[i][k] == -1 or self.matriz[k][j] == -1:
                            self.matriz[i][j] = -1
                        else:
                            self.matriz[i][j] += max(self.matriz[i][k], self.matriz[k][j])

    def verificar_mao_dupla(self):
        matriz_transposta = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                linha.append(0)
            matriz_transposta.append(linha)

        for i in range(self.n):
            for j in range(self.n):
                matriz_transposta[i][j] = self.matriz[j][i]

        for i in range(self.n):
            for j in range(self.n):
                if matriz_transposta[i][j] == self.matriz[i][j] and self.matriz[i][j] == 1:
                    self.matriz[i][j] = -1


    def imprimir_matriz(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])

def main():
    grafo = Grafo("Ex4.txt")
    grafo.verificar_mao_dupla()
    grafo.floyd_warshall()
    grafo.imprimir_matriz()

if __name__ == "__main__":
    main()
