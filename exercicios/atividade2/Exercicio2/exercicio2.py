# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        # Indice do vertice
        self.indice = i
        self.parentes = []
        # Tempo de descoberta de cada vertice
        self.tempo = -1
        # Numero de pre-ordem minimo (Lowest preorder number)
        self.low = float("inf")
    
    def get_indice(self):
        return self.indice

    def get_parentes(self):
        return self.parentes

    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, novo_tempo):
        self.tempo = novo_tempo

# Classe que representa o grafo
class Grafo:
    # n eh a quantidade de vertices
    def __init__(self, n):
        # Instancia a lista de adjacencia
        self.lista_adjacencia = []
        for i in range(n):
            self.lista_adjacencia.append([])
        # Define a quantidade de vertices do grafo
        self.quantidade_vertices = n
        # Instancia a lista de vertices
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(Vertice(i))

    def adiciona_aresta(self, v, u):
        self.lista_adjacencia[v].append(u)
        self.lista_adjacencia[u].append(v)
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices

    def get_lista_adjacencia(self):
        return self.lista_adjacencia
    
    def get_lista_vertices(self):
        return self.lista_vertices

def retorna_ponte(grafo, vertice1, vertice2):
    

def leitura_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")

    linha = arquivo.readline()
    valores = linha.split()

    numero_vertices = int(valores[0])
    numero_arestas = int(valores[1])
    
    grafo = Grafo(numero_vertices)

    for i in range(numero_arestas):
        linha = arquivo.readline()
        valores = linha.split()
        
        # Eh necessario subtrair uma unidade dos indices dos vertices
        # Pois esse algoritmo considera que o primeiro vertice eh o vertice 0 (zero)
        # Sendo assim, o primeiro vertice eh o vertice 0
        # O segundo vertice eh o vertice 1
        # O terceito vertice eh o vertice 2
        # E assim por diante
        grafo.get_lista_adjacencia()[int(valores[0])-1].append(int(valores[1])-1)
        
    return grafo

# Funcao principal
def main():
    grafo = leitura_arquivo("grafo1.txt")
    for i in range(grafo.get_quantidade_vertices()):
        for adjacente in grafo.get_lista_adjacencia()[i]:
            print("{} - {}".format(i, adjacente))

if __name__ == "__main__":
    main()
