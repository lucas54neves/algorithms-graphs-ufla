'''
Resposta em Python
GCC218 - 2019/02
Atividade: 
Grupo:
    Lucas Neves, 14A, 201720357
    Davi Horner, 10A, 201720368
    Thiago Luigi, 10A, 201720364
Data: 06/09/2019  
'''

from collections import deque

class Grafo:
    def __init__(self, n):
        # Cria a lista de adjacencia
        self.lista_adj = []
        for i in range(n):
            self.lista_adj.append([])
        self.quantidade_vertices = n
        # Cria a lista de vertices
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(Vertice(i))
    
    def get_lista_adj(self):
        return self.lista_adj
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices
    
    def get_lista_vertices(self):
        return self.lista_vertices

class Vertice:
    def __init__(self, x):
        self.id = x
        self.cor = "branco"
        self.distancia = float("inf")
        self.predecessor = None
        self.dominante = None
        self.f = float("inf")
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    
    def set_distancia(self, nova_distancia):
        self.distancia = nova_distancia
    
    def set_predecessor(self, novo_predecessor):
        self.predecessor = novo_predecessor
    
    def set_dominante(self, novo_dominante):
        self.dominante = novo_dominante
    
    def set_f(self, novo_f):
        self.f = novo_f
    
    def get_id(self):
        return self.id
    
    def get_cor(self):
        return self.cor
    
    def get_distancia(self):
        return self.distancia
    
    def get_predecessor(self):
        return self.predecessor
    
    def get_dominante(self):
        return self.dominante
    
    def get_f(self):
        return self.f

def leGrafo():
    arquivo = open('ativ1_instance.txt', 'r')
    
    # Le do arquivo a quantidade de vertices
    # Sendo n a quantidade de vertices
    linha = arquivo.readline()
    n = int(linha)
    
    # Cria o grafo
    grafo = Grafo(n)
    
    # Le todos os vertices adjacentes e guarda na lista
    linha = arquivo.readline()

    while linha:
        valores = linha.split()
        
        # Pega o vertice que vai ser a posicao na lista
        # Os vertices seguintes sao adjacentes a esse vertice
        vertice = Vertice(int(valores.pop(0)))
        
        while valores != []:
            adjacente = valores.pop(0)
            if adjacente != '-':
                grafo.get_lista_adj()[vertice.get_id()].append(Vertice(int(adjacente)))
        
        linha = arquivo.readline()
    
    vertice_inicial = Vertice(0)
    abordagem1(grafo)
    abordagem2(grafo, vertice_inicial)

def dfs(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("branco")
        grafo.get_lista_vertices()[i].set_predecessor(None)
    
    for i in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[i].get_cor() == "branco":
            dfsVisit(grafo, grafo.get_lista_vertices()[i].get_id())
    
def dfsVisit(grafo, id_vertice):
    global tempo
    tempo = tempo + 1
    
    grafo.get_lista_vertices()[id_vertice].set_distancia(tempo)
    grafo.get_lista_vertices()[id_vertice].set_cor("cinza")
    
    for i in range(len(grafo.get_lista_adj()[id_vertice])):
        # Pega o id do vertice adjacente e confere os dados desse vertice na lista de adjacencia
        if grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i].get_id()].get_cor() == "branco":
            grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i].get_id()].set_predecessor(grafo.get_lista_vertices()[id_vertice].get_id())
            dfsVisit(grafo, grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i].get_id()].get_id())
    
    grafo.get_lista_vertices()[id_vertice].set_cor("preto")
    tempo = tempo + 1
    grafo.get_lista_vertices()[id_vertice].set_f(tempo)

# Imprime os vertices dominantes usando DFS
def abordagem1(grafo):
    dfs(grafo)
    
    print("Abordagem 1 - DFS")
    #for i in range(grafo.get_quantidade_vertices()):
        #print(grafo.get_lista_vertices()[i].get_distancia(), grafo.get_lista_vertices()[i].get_f())
    
    i = 0
    while i < (grafo.get_quantidade_vertices() - 1):
        j = i + 1
        while j < (grafo.get_quantidade_vertices()):
            if grafo.get_lista_vertices()[i].get_distancia() < grafo.get_lista_vertices()[j].get_distancia() and grafo.get_lista_vertices()[i].get_f() > grafo.get_lista_vertices()[j].get_f():
                grafo.get_lista_vertices()[j].set_dominante(i)
            j = j + 1
        i = i + 1
    
    for k in range(grafo.get_quantidade_vertices()):
        print("Vertice {} - Dominante {}".format(grafo.get_lista_vertices()[k].get_id(), grafo.get_lista_vertices()[k].get_dominante()))

# Imprime os vertices dominantes usando BFS
def abordagem2(grafo, fonte):
    predecessores = []
    for i in range(grafo.get_quantidade_vertices()):
        predecessores.append([])
    
    fonte.set_cor("cinza")
    fonte.set_distancia(0)
    
    q = deque()
    
    q.append(fonte)
    
    while len(q) > 0:
        u = q.popleft()
        
        i = 0
        for vertice in grafo.get_lista_adj()[u.get_id()]:
            v = grafo.get_lista_adj()[u.get_id()][i]
            if v.get_cor() == "branco":
                v.set_cor("cinza")
                v.set_distancia(u.get_distancia()+1)
                v.set_predecessor(u)
                predecessores[v.get_id()].append(u.get_id())
                q.append(v)
            i = i + 1
        
        u.set_cor("preto")
    
    print("Abordagem 2 - BFS")
    for i in range (len(predecessores)):
        if len(predecessores[i]) > 1:
            print('Vertice {} - Dominante {}'.format(i, i))
        elif len(predecessores[i]) == 1:
            print('Vertice {} - Dominante {}'.format(i, predecessores[i][0]))
        else:
            print('Vertice {} - Dominante nulo'.format(i))

# Funcao principal
def main():
    leGrafo()

if __name__ == "__main__":
    tempo = 0
    main()
