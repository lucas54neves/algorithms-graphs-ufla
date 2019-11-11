class Vertice:
    def __init__(self, indice):
        self.indice = indice
        self.tempo_inicial = -1
        self.tempo_final = -1
        self.cor = "branco"
        self.adjacentes = []

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

class Grafo:
    def __init__(self, nome_arquivo):
        self.vertices = []
        self.tempo = 0
        self.ler_arquivo(nome_arquivo)
        self.dfs()
        self.vertices.sort(key=lambda x: x.tempo_final, reverse=True)
        self.imprimir_resultado()

    def ler_arquivo(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')

        linha = arquivo.readline()

        self.n = int(linha)

        for i in range(self.n):
            self.vertices.append(Vertice(i))

        linha = arquivo.readline()

        while linha:
            valores = linha.split()

            vertice1 = int(valores[0])
            vertice2 = int(valores[1])

            self.adicionar_adjacente(self.vertices[vertice1], self.vertices[vertice2])
            linha = arquivo.readline()

    def adicionar_adjacente(self, vertice1, vertice2):
        vertice1.adicionar_adjacente(vertice2)

    def dfs(self):
        for i in range(self.n):
            if self.vertices[i].cor == "branco":
                self.dfs_visit(self.vertices[i])

    def dfs_visit(self, vertice):
        self.tempo += 1

        vertice.cor = "cinza"
        vertice.tempo_inicial = self.tempo

        for adjacente in vertice.adjacentes:
            if adjacente.cor == "branco":
                self.dfs_visit(adjacente)

        vertice.cor = "preto"

        self.tempo += 1

        vertice.tempo_final = self.tempo

    def imprimir_resultado(self):
        retorno = ""
        for vertice in self.vertices:
            retorno += str(vertice.indice) + " "
        print(retorno)

def main():
    grafo = Grafo("Ex2.txt")

if __name__ == "__main__":
    main()
