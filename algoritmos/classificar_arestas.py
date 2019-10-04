from grafo import *
from entrar_grafo import entrar_grafo

def dfs(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("branco")
        grafo.get_lista_vertices()[i].set_pai(None)

    for i in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[i].get_cor() == "branco":
            dfs_visit(grafo, i)

def dfs_visit(grafo, indice_vertice):
    grafo.incrementar_tempo()

    grafo.get_lista_vertices()[indice_vertice].set_tempo_inicial(grafo.get_tempo())
    grafo.get_lista_vertices()[indice_vertice].set_cor("cinza")

    for adjacente in grafo.get_lista_adjacencia()[indice_vertice]:
        if grafo.get_lista_vertices()[adjacente].get_cor() == "branco":
            print("{} - {} = Aresta de arvore".format(indice_vertice, adjacente))
            grafo.get_lista_vertices()[adjacente].set_pai(indice_vertice)
            dfs_visit(grafo, adjacente)
        elif grafo.get_lista_vertices()[adjacente].get_cor() == "cinza":
            print("{} - {} = Aresta de retorno".format(indice_vertice, adjacente))
        elif grafo.get_lista_vertices()[adjacente].get_cor() == "preto":
            if grafo.get_lista_vertices()[indice_vertice].get_tempo_inicial() < grafo.get_lista_vertices()[adjacente].get_tempo_final():
                print("{} - {} = Aresta direta".format(indice_vertice, adjacente))
            else:
                print("{} - {} = Aresta cruzada".format(indice_vertice, adjacente))

    grafo.get_lista_vertices()[indice_vertice].set_cor("preto")
    grafo.incrementar_tempo()
    grafo.get_lista_vertices()[indice_vertice].set_tempo_final(grafo.get_tempo())

# Funcao principal para teste
def main():
    grafo = entrar_grafo()
    dfs(grafo)

if __name__ == "__main__":
    main()
