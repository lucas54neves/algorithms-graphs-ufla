class Grafo:
    def __init__(self, nome_arquivo):
        self.arestas = []
        self.caminho = []
        self.graus = []
        self.n = 0
        self.ler_arquivo(nome_arquivo)

    def ler_arquivo(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')

        linha = arquivo.readline()

        self.n = int(linha)

        linha = arquivo.readline()

        while linha:
            valores = linha.split()

            vertice1 = int(valores[0])
            vertice2 = int(valores[1])

            self.adicionar_aresta(vertice1, vertice2)
            linha = arquivo.readline()

    def adicionar_aresta(self, vertice1, vertice2):
        self.arestas.append([vertice1, vertice2])

    def hierholzer(self, vertice):
        for aresta in self.arestas:
            if vertice == aresta[0]:
                self.arestas.remove(aresta)
                self.hierholzer(aresta[1])
            elif vertice == aresta[1]:
                self.arestas.remove(aresta)
                self.hierholzer(aresta[0])
        self.caminho.append(vertice)

    def imprimir_resultado(self):
        self.caminho.reverse()
        retorno = ""
        for vertice in self.caminho:
            retorno += " " + str(vertice)
        print(retorno)


    def verificar_pares(self):
        for i in range(self.n):
            self.graus.append(0)

        for i,j in self.arestas:
            self.graus[i] += 1
            self.graus[j] += 1

        for i in self.graus:
            if i % 2 == 1:
                return False

        return True

    def algoritmo(self):
        if self.verificar_pares():
            self.hierholzer(0)
            self.imprimir_resultado()
        else:
            print("Grafo Nao Euleriano")

def main():
    grafo = Grafo("Ex1.txt")
    grafo.algoritmo()

if __name__ == "__main__":
    main()
