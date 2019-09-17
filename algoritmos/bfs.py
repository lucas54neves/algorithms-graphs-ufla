from collections import deque

def bfs(grafo, id_fonte):
    i = 0
    while i < grafo.get_quantidade_vertices():
        if i != id_fonte:
            grafo.get_lista_vertices()[i].set_cor("branco")
            grafo.get_lista_vertices()[i].set_distancia(float("inf"))
            grafo.get_lista_vertices()[i].set_predecessor(None)
        i = i + 1
    
    grafo.get_lista_vertices()[id_fonte].set_cor("cinza")
    grafo.get_lista_vertices()[id_fonte].set_distancia(0)
    grafo.get_lista_vertices()[id_fonte].set_predecessor(None)
    
    q = deque()
    
    q.append(id_fonte)
    
    while len(q) > 0:
        u = q.popleft()
        
        i = 0
        for vertice_adjacente in grafo.get_lista_adj()[u]:
            v = grafo.get_lista_adj()[u][i]
            
            if grafo.get_lista_vertices()[v].get_cor() == "branco":
                grafo.get_lista_vertices()[v].set_cor("cinza")
                grafo.get_lista_vertices()[v].set_distancia(grafo.get_lista_vertices()[u].get_distancia() + 1)
                grafo.get_lista_vertices()[v].set_predecessor(u)
                q.append(v)
            
            i = i + 1
        
        grafo.get_lista_vertices()[u].set_cor("preto") 
