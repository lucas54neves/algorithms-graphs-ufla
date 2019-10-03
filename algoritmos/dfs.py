from grafo import *

def dfs(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("branco")
        grafo.get_lista_vertices()[i].set_pai(None)
    
    for i in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[i].get_cor() == "branco":
            dfs_visit(grafo, i)
    
    print("Resultado da Busca em Produndidade")
    for i in range(grafo.get_quantidade_vertices()):
        print("Vertice: {} - Tempo inicial: {} - Tempo final: {}".format(grafo.get_lista_vertices()[i].get_indice(), grafo.get_lista_vertices()[i].get_tempo_inicial(), grafo.get_lista_vertices()[i].get_tempo_final()))

def dfs_visit(grafo, indice_vertice):
    grafo.incrementar_tempo()
    
    grafo.get_lista_vertices()[indice_vertice].set_tempo_inicial(grafo.get_tempo())
    grafo.get_lista_vertices()[indice_vertice].set_cor("cinza")
    
    for adjacente in grafo.get_lista_adjacencia()[indice_vertice]:
        if grafo.get_lista_vertices()[adjacente].get_cor() == "branco":
            grafo.get_lista_vertices()[adjacente].set_pai(indice_vertice)
            dfs_visit(grafo, adjacente)
    
    grafo.get_lista_vertices()[indice_vertice].set_cor("preto")
    grafo.incrementar_tempo()
    grafo.get_lista_vertices()[indice_vertice].set_tempo_final(grafo.get_tempo())

# Funcao principal para teste
def main():
    grafo = Grafo(4)
    grafo.adicionar_aresta_direcional(0, 1)
    grafo.adicionar_aresta_direcional(0, 3)
    grafo.adicionar_aresta_direcional(1, 2)
    grafo.adicionar_aresta_direcional(2, 3)
    grafo.adicionar_aresta_direcional(3, 1)
    dfs(grafo)

if __name__ == "__main__":
    main()
