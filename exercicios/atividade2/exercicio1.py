'''
Resposta em Python
GCC218 - 2019/02
Atividade: Implementacao 2 (Exercicio1)
Grupo:
    Lucas Neves, 14A, 201720357
    Davi Horner, 10A, 201720368
    Thiago Luigi, 10A, 201720364
Data: 20/09/2019  
'''

from collections import deque

# Classe que representa o vertice
class Vertice:
    def __init__(self, i):
        # Indice do vertice
        self.indice = i
        self.cor = -1
    
    def get_indice(self):
        return self.indice

    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor

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
    
    def get_quantidade_vertices(self):
        return self.quantidade_vertices

    def get_lista_adjacencia(self):
        return self.lista_adjacencia
    
    def get_lista_vertices(self):
        return self.lista_vertices

# A cor 0 eh azul e a cor 1 eh rosa
def colore(grafo, vertice_inicial):
    grafo.get_lista_vertices()[vertice_inicial].set_cor(0)

    fila = deque()
    
    fila.append(vertice_inicial)

    while len(fila) > 0:
        u = fila.popleft()

        i = 0
        for vertice_adjacente in grafo.get_lista_adjacencia()[u]:
            v = grafo.get_lista_adjacencia()[u][i]

            if grafo.get_lista_vertices()[v].get_cor() == -1:
                # Isso faz com que a cor de v seja oposta da cor de u
                grafo.get_lista_vertices()[v].set_cor(1 - grafo.get_lista_vertices()[u].get_cor())

                #Adiciona o v na lista da BFS
                fila.append(v)
            
            i = i + 1

def checa_bipardido(grafo):
    for vertice in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[vertice].get_cor() == -1:
            colore(grafo, vertice)

    for vertice in range(grafo.get_quantidade_vertices()):
        for adjacente in grafo.get_lista_adjacencia()[vertice]:
            if grafo.get_lista_vertices()[vertice].get_cor() == grafo.get_lista_vertices()[adjacente].get_cor():
                # Se dois vizinhos possuirem a mesma coisa, o grafo nao eh bipartido
                return False
    
    # Se nada estiver errado, o grafo eh bipartido
    return True

def leitura_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")

    numero_vertices = int(arquivo.readline())
    numero_arestas = int(arquivo.readline())
    
    grafo = Grafo(numero_vertices)
    
    for i in range(numero_arestas):
        linha = arquivo.readline()
        valores = linha.split()
        grafo.get_lista_adjacencia()[int(valores[0])].append(int(valores[1]))
    
    return grafo

def executa(nome_arquivo):
    grafo = leitura_arquivo(nome_arquivo)
    if checa_bipardido(grafo):
        print("SIM")
    else:
        print("NAO")

# Funcao principal
def main():
    executa("grafo1.txt")
    executa("grafo2.txt")
    executa("grafo3.txt")

if __name__ == "__main__":
    main()
