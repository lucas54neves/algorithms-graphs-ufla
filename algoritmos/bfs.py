from collections import deque
from grafo import *
from entrar_grafo import entrar_grafo

def bfs(grafo, id_fonte):
    i = 0
    while i < grafo.get_quantidade_vertices():
        if i != id_fonte:
            grafo.get_lista_vertices()[i].set_cor("branco")
            grafo.get_lista_vertices()[i].set_distancia(float("inf"))
            grafo.get_lista_vertices()[i].set_pai(None)
        i = i + 1
    
    grafo.get_lista_vertices()[id_fonte].set_cor("cinza")
    grafo.get_lista_vertices()[id_fonte].set_distancia(0)
    grafo.get_lista_vertices()[id_fonte].set_pai(None)
    
    q = deque()
    
    q.append(id_fonte)
    
    while len(q) > 0:
        u = q.popleft()
        
        i = 0
        for vertice_adjacente in grafo.get_lista_adjacencia()[u]:
            v = grafo.get_lista_adjacencia()[u][i]
            
            if grafo.get_lista_vertices()[v].get_cor() == "branco":
                grafo.get_lista_vertices()[v].set_cor("cinza")
                grafo.get_lista_vertices()[v].set_distancia(grafo.get_lista_vertices()[u].get_distancia() + 1)
                grafo.get_lista_vertices()[v].set_pai(u)
                q.append(v)
            
            i = i + 1
        
        grafo.get_lista_vertices()[u].set_cor("preto") 
    
    print("Resultado da Busca em Largura")
    for i in range(grafo.get_quantidade_vertices()):
        print("Vertice: {} - Distancia: {}".format(grafo.get_lista_vertices()[i].get_indice(), grafo.get_lista_vertices()[i].get_distancia()))

# Funcao principal para teste
def main():
    grafo = entrar_grafo()
    bfs(grafo, 0)

if __name__ == "__main__":
    main()
