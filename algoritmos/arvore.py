from grafo import *

def arvore(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("branco")
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("cinza")
        for adjacente in grafo.get_lista_adjacencia()[i]:
            if grafo.get_lista_vertices()[adjacente].get_cor() == "cinza":
                return False
            grafo.get_lista_vertices()[adjacente].set_cor("cinza")
    return True
    

grafo = Grafo(3)
grafo.adicionar_aresta_nao_direcional(0, 1)
grafo.adicionar_aresta_nao_direcional(0, 2)
#grafo.adicionar_aresta_nao_direcional(1, 2)

print(arvore(grafo))
