from collections import deque

# Classe que representa o grafo
class Grafo:
    def __init__(self, n):
        self.quantidade_vertices = n
        self.lista_adjacencia = []
        for i in range(self.quantidade_vertices):
            self.lista_adjacencia.append(deque())

    def adicionar_aresta(self, u, v):
        self.lista_adjacencia[u].append(v)

    def hierholzer(self):
        # grau[i] representa o grau do vertice i
        arestas = []
        for i in range(self.quantidade_vertices):
            arestas.append(len(self.lista_adjacencia[i]))

        # Pilha para o circuito atual
        caminho_atual = []

        # Lista para o circuito final
        circuito = []

        # Inicia com o vertice 0
        vertice_atual = 0
        caminho_atual.append(0)

        while len(caminho_atual) != 0:
            if arestas[vertice_atual] > 0:
                # Adiciona o vertice atual
                caminho_atual.append(vertice_atual)

                # Encontra o proximo vertice usando a aresta
                proximo_vertice = self.lista_adjacencia[vertice_atual].popleft()

                # Remove a aresta
                arestas[vertice_atual] -= 1

                # Move para o proximo vertice
                vertice_atual = proximo_vertice
            else:
                circuito.append(vertice_atual)
                vertice_atual = caminho_atual.pop()

        resultado = ""
        i = len(circuito)
        while i >= 0:
            if len(circuito) > 0:
                resultado += str(circuito.pop())
            if i > 1:
                resultado += " -> "
            i -= 1

        print(resultado)

grafo1 = Grafo(3)
grafo1.adicionar_aresta(0,1)
grafo1.adicionar_aresta(1,2)
grafo1.adicionar_aresta(2,0)
grafo1.hierholzer()

grafo2 = Grafo(7)
grafo2.adicionar_aresta(0,1)
grafo2.adicionar_aresta(0,6)
grafo2.adicionar_aresta(1,2)
grafo2.adicionar_aresta(2,0)
grafo2.adicionar_aresta(2,3)
grafo2.adicionar_aresta(3,4)
grafo2.adicionar_aresta(4,2)
grafo2.adicionar_aresta(4,5)
grafo2.adicionar_aresta(5,0)
grafo2.adicionar_aresta(6,4)
grafo2.hierholzer()
