# Classe que representa o vertice adjacente
class Adjacente:
    def __init__(self, i):
        # Indice do vertice adjacente
        self.indice = i
        # Atributo que informa se a aresta foi visitada
        self.visitada = False

    def get_indice(self):
        return self.indice

    def get_visitada(self):
        return self.visitada

    def visitar(self):
        self.visitada = True

# Classe que representa o grafo
class Grafo:
    def __init__(self, nome_arquivo):
        arquivo = open(nome_arquivo, "r")
        # Quantidade de vertices
        self.quantidade_vertices = int(arquivo.readline())
        # Lista de adjacencia dos vertices
        self.lista_adjacencia = []
        for i in range(self.quantidade_vertices):
            self.lista_adjacencia.append([])
        # Adiciona as arestas apartir do arquivo
        for linha in arquivo:
            valores = linha.split()
            self.adicionar_aresta(int(valores[0]), int(valores[1]))

    def adicionar_aresta(self, u, v):
        self.lista_adjacencia[u].append(Adjacente(v))

    def hierholzer(self):
        # Vertice inicial do algoritmo
        # Escolhido aleatoriamente
        vertice_inicial = random.randint(0, self.quantidade_vertices)

        # Armazena o circuito
        circuito = []

        while circuito:
            pass

    # Metodo para imprimir o resultado de acordo com o que pede no enunciado
    # O circuito euleriano ou a mensagem "Grafo Nao Euleriano"
    def imprimir_resultado(self):
        pass

grafo = Grafo("Ex1.txt")
#grafo.hierholzer()
#grafo.imprimir_resultado()
