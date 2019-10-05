# Classe para representar o grafo
class Grafo:
    def __init__(self, n):
        # Quantidade n de vertices
        self.quantidade_vertices = n

        # Lista para armazenas as arestas
        self.arestas = []

    # Para adicionar a aresta ao grafo
    # vertice_i = indice do vertice i
    # vertice_j = indice do vertice j
    # peso = peso da aresta
    def adicionar_aresta(self, vertice_i, vertice_j, peso):
        self.arestas.append([vertice_i, vertice_j, peso])

    # Usando a compressao de caminho
    # Para encontrar o representante do (unico) conjunto que contem i
    def encontrar(self, pai, i):
        if i != pai[i]:
            return self.encontrar(pai, pai[i])
        else:
            return i

    # O posto de i eh o limite superior para a altura de i
    def unir(self, pai, posto, x, y):
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)

        # A raiz que ocupa o menor posto aponta para a raiz que ocupa o maior posto
        if posto[raiz_x] < posto[raiz_y]:
            pai[raiz_x] = raiz_y
        elif posto[raiz_x] > posto[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            posto[raiz_x] += 1

    def kruskall(self):
        # lista para a arvore geradora minima resultante do algoritmo
        arvore = []

        # Ordena as arestas por tamanho
        self.arestas.sort(key=lambda item: item[2])

        # Vetor dos pais de cada vertice
        pai = []

        # Vetor para o posto de cada vertice
        posto = []

        # Cada vertice se torna uma arvore com um unico vertice
        # Ou seja, o vertice i passa a ser membro do conjunto cujo unico membro eh i
        for vertice in range(self.quantidade_vertices):
            pai.append(vertice)
            posto.append(0)

        # O algoritmo roda ate a arvore possuir n - 1 arestas
        # Seguindo a definicao de arvore
        while len(arvore) < self.quantidade_vertices - 1:
            u, v, w = self.arestas.pop(0)
            x = self.encontrar(pai, u)
            y = self.encontrar(pai, v)

            if x != y:
                arvore.append([u, v, w])
                self.unir(pai, posto, x, y)

        print("AGM resultante do Algorimo de Kruskall")
        print("Vertice u - Vertice v : Peso da aresta")
        for u, v, w in arvore:
            print("{} - {} : {}".format(u, v, w))

grafo = Grafo(9)
grafo.adicionar_aresta(0,1,4)
grafo.adicionar_aresta(0,7,8)
grafo.adicionar_aresta(1,2,8)
grafo.adicionar_aresta(1,7,11)
grafo.adicionar_aresta(2,3,7)
grafo.adicionar_aresta(2,8,2)
grafo.adicionar_aresta(2,5,4)
grafo.adicionar_aresta(3,4,9)
grafo.adicionar_aresta(3,5,14)
grafo.adicionar_aresta(5,6,2)
grafo.adicionar_aresta(6,8,6)
grafo.adicionar_aresta(6,7,1)
grafo.adicionar_aresta(7,8,7)
grafo.adicionar_aresta(4,5,10)
grafo.kruskall()
