import math

class Vertice:
    def __init__(self, identificador, coordenada_x, coordenada_y):
        self.identificador = identificador
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.tempo = float("inf")
        self.arestas = []
        self.pai = None

    def adicionar_aresta(self, destino, tempo):
        self.arestas.append((destino, tempo))

    def relaxar_adjacentes(self):
        for destino, tempo in self.arestas:
            if destino.tempo > self.tempo + tempo:
                destino.tempo = self.tempo + tempo
                destino.pai = self

class Grafo:
    def __init__(self, nome_arquivo):
        # Lista para armazenar os vertices
        self.vertices = []
        # Metodo que le o arquivo
        self.ler_arquivo(nome_arquivo)
        # Metodo que cria as arestas
        self.criar_arestas()
        # Aplica o algoritmo de Bellman-Ford
        self.bellman_ford()
        # Imprime o resultado como pede o enunciado
        self.imprimir_resultado()

    def ler_arquivo(self, nome_arquivo):
        # Abre o arquivo
        arquivo = open(nome_arquivo, 'r')

        linha = arquivo.readline()
        valores = linha.split()

        # Adiciona o vertice que representa a casa
        self.adicionar_vertice(Vertice(0, int(valores[0]), int(valores[1])))

        # Pega o vertice que representa a escola
        # Esse vertice sera adicionado no final da lista dos vertices
        escola = Vertice(0, int(valores[2]), int(valores[3]))

        # Leitura das coordenadas das linhas de metro
        # i representa i identificador de cada linha de metro
        linha = arquivo.readline()
        i = 1
        while linha:
            valores = linha.split()

            while valores:
                coordenada_x, coordenada_y = int(valores.pop(0)), int(valores.pop(0))

                if coordenada_x != -1 and coordenada_y != -1:
                    self.adicionar_vertice(Vertice(i, coordenada_x, coordenada_y))

            linha = arquivo.readline()
            i += 1

        # Adiciona o vertice que representa a escola no final da lista
        self.adicionar_vertice(escola)

    def adicionar_vertice(self, vertice):
        self.vertices.append(vertice)

    def criar_arestas(self):
        for vertice1 in self.vertices:
            for vertice2 in self.vertices:
                if vertice1 != vertice2:
                    if vertice1.identificador == 0:
                        vertice1.adicionar_aresta(vertice2, self.calcular_tempo(vertice1, vertice2, 1.7))
                    elif vertice1.identificador == vertice2.identificador:
                        vertice1.adicionar_aresta(vertice2, self.calcular_tempo(vertice1, vertice2, 3.1111))
                    else:
                        vertice1.adicionar_aresta(vertice2, self.calcular_tempo(vertice1, vertice2, 1.7))

    def calcular_tempo(self, vertice1, vertice2, velocidade):
        return math.ceil((self.calcular_distancia(vertice1, vertice2) / velocidade) / 60.0)

    def calcular_distancia(self, vertice1, vertice2):
        return math.sqrt(math.pow((vertice1.coordenada_x - vertice2.coordenada_x), 2) + math.pow((vertice1.coordenada_y - vertice2.coordenada_y), 2))

    def bellman_ford(self):
        self.vertices[0].tempo = 0

        for vertice in self.vertices:
            vertice.relaxar_adjacentes()

    def imprimir_resultado(self):
        print(self.vertices[len(self.vertices) - 1].tempo)

def main():
    grafo = Grafo("Ex3.txt")

if __name__ == "__main__":
    main()
