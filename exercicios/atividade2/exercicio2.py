'''
Resposta em Python
GCC218 - 2019/02
Atividade: Implementacao 2 (Exercicio2)
Grupo:
    Lucas Neves, 14A, 201720357
    Davi Horner, 10A, 201720368
    Thiago Luigi, 10A, 201720364
Data: 20/09/2019  
'''

# Classe que representa a aresta percorrida
class Aresta:
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
    
    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino

# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        # Indice do vertice
        self.indice = i
        # Vertice "pai" do vertice durante o percuso da busca em profundidade        
        self.pai = -1
        # Tempo de descoberta de cada vertice
        self.tempo = float("inf")
        # Numero de pre-ordem minimo (Lowest preorder number)
        self.low = float("inf")
        # Se vertice foi visitado
        self.visitado = False
    
    def get_indice(self):
        return self.indice

    def get_pai(self):
        return self.pai

    def set_pai(self, padrasto):
        self.pai = padrasto

    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, novo_tempo):
        self.tempo = novo_tempo

    def get_low(self):
        return self.low
    
    def set_low(self, novo_low):
        self.low = novo_low

    def get_visitado(self):
        return self.visitado
    
    def set_visitado(self, novo_visitado):
        self.visitado = novo_visitado

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
        self.tempo = 0
        self.Aresta = []

    def adiciona_aresta(self, v, u):
        self.lista_adjacencia[v].append(u)
        self.lista_adjacencia[u].append(v)
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices

    def get_lista_adjacencia(self):
        return self.lista_adjacencia
    
    def get_lista_vertices(self):
        return self.lista_vertices

    def get_tempo(self):
        return self.tempo

    def set_tempo(self, novo_tempo):
        self.tempo = novo_tempo

    def get_Aresta(self):
        return self.Aresta

    def set_Aresta(self, u, v):
        self.Aresta.append(Aresta(u, v))
    
    # Impressao do resultado
    # Como a saida do enunciado esta em ordem crescente primeiro da origem da aresta e depois do destino
    # A lista do caminho eh ordenada, primeiramente usando o vertice de destino como chave e depois o vertice de origem
    def imprime_resultado(self):
        self.get_Aresta().sort(key=lambda a: a.get_destino())
        self.get_Aresta().sort(key=lambda a: a.get_origem())
        for j in self.get_Aresta():
            print("{} {}".format(j.get_origem(), j.get_destino()))

# Funcao para encontrar as pontes
# Baseado na busca em profundidade
def ponte(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[i].get_visitado() == False:
            ponte_auxiliar(grafo, i)

# Funcao auxiliar para encontrar as pontes
def ponte_auxiliar(grafo, vertice):
    grafo.get_lista_vertices()[vertice].set_visitado(True)
    grafo.get_lista_vertices()[vertice].set_tempo(grafo.get_tempo())
    grafo.get_lista_vertices()[vertice].set_low(grafo.get_tempo())
    grafo.set_tempo(grafo.get_tempo()+1)

    for adjacente in grafo.get_lista_adjacencia()[vertice]:
        if grafo.get_lista_vertices()[adjacente].get_visitado() == False:
            grafo.get_lista_vertices()[adjacente].set_pai(vertice)
            ponte_auxiliar(grafo, adjacente)
            
            grafo.get_lista_vertices()[vertice].set_low(min(grafo.get_lista_vertices()[vertice].get_low(), grafo.get_lista_vertices()[adjacente].get_low()))
            
            # Se for ponte, pega a aresta de ida e volta
            # A rua continua dupla
            if grafo.get_lista_vertices()[adjacente].get_low() > grafo.get_lista_vertices()[vertice].get_tempo():             
                grafo.set_Aresta(adjacente+1, vertice+1)                
                grafo.set_Aresta(vertice+1, adjacente+1)                                
            # Se nao for ponte, pega a aresta de ida
            # A rua se torna mao-unica
            else:
                grafo.set_Aresta(vertice+1, adjacente+1)
    
        elif adjacente != grafo.get_lista_vertices()[vertice].get_pai():
            grafo.get_lista_vertices()[vertice].set_low(min(grafo.get_lista_vertices()[vertice].get_low(), grafo.get_lista_vertices()[adjacente].get_tempo()))
            # Se a aresta for cruzada e o vertice adjacente nao for pai do vertice, a rua se torna simples
            # Pega a aresta de ida
            if grafo.get_lista_vertices()[vertice].get_tempo() > grafo.get_lista_vertices()[adjacente].get_tempo():
                grafo.set_Aresta(vertice+1, adjacente+1)

# Funcao para a leitura do arquivo
def leitura_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")

    linha = arquivo.readline()
    valores = linha.split()

    # Pega a quantidade de vertices e de arestas
    numero_vertices = int(valores[0])
    numero_arestas = int(valores[1])
    
    # Cria o grafo que sera usado no sistema
    grafo = Grafo(numero_vertices)

    # Leitura das arestas
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
        grafo.get_lista_adjacencia()[int(valores[1])-1].append(int(valores[0])-1)
    
    # Retorna o grafo criado 
    return grafo

# Funcao que executa o sistema
# Primeiro o grafo eh lido atraves do arquivo texto
# Depois a funcao que encontra as pontes eh executada
# Depois o resultado eh impresso
def executa(nome_arquivo):
    grafo = leitura_arquivo(nome_arquivo)
    ponte(grafo)
    grafo.imprime_resultado()

# Funcao principal
def main():
    print("Grafo 1")
    executa("grafo1.txt")
    print("Grafo 2")
    executa("grafo2.txt")

if __name__ == "__main__":
    main()
