class Vertice:
    def __init__(self, indice):
        self.indice = indice
        self.adjacentes = []

    def adicionar_aresta(self, adjacente):
        self.adjacentes.append(adjacente)

class Grafo:
    def __init__(self, nome_arquivo):
        self.ler_arquivo(nome_arquivo)

    def ler_arquivo(self, nome_arquivo):
        # Abre o arquivo para leitura
        arquivo = open(nome_arquivo, 'r')

        # Lista para armazenar os vertices do grafo
        self.vertices = []

        # Lista para armazenar o caminho euleriano
        self.caminho_euleriano = []

        linha = arquivo.readline()
        valores = linha.split()

        # Variavel que armazena a quantidade de vertices do grafo
        self.n = int(valores[0])

        # Inicializa todos os vertices
        for i in range(self.n):
            self.vertices.append(Vertice(i))

        linha = arquivo.readline()
        while linha:
            valores = linha.split()

            # Adiciona todas as arestas do grafo
            self.adicionar_aresta(int(valores[1]),int(valores[0]))

            linha = arquivo.readline()

    def adicionar_aresta(self, vertice1, vertice2):
        self.vertices[vertice1].adicionar_aresta(vertice2)
        self.vertices[vertice2].adicionar_aresta(vertice1)

    def remover_aresta(self, vertice1, vertice2):
        self.vertices[vertice1].adjacentes.remove(vertice2)
        self.vertices[vertice2].adjacentes.remove(vertice1)

    def imprimir_resultado(self):
        i = len(self.caminho_euleriano) - 1
        if self.caminho_euleriano[0] == self.caminho_euleriano[i]:
            print(self.caminho_euleriano)
        else:
            print("Grafo Nao Euleriano")

    def hierholzer(self, vertice):
        for adjacente in self.vertices[vertice].adjacentes:
            self.remover_aresta(vertice, adjacente)
            self.hierholzer(adjacente)
        self.caminho_euleriano.append(vertice)

def main():
    grafo = Grafo("Ex1.txt")
    grafo.hierholzer(0)
    grafo.imprimir_resultado()

if __name__ == "__main__":
    main()
