from grafo import *

def arvore_auxiliar(grafo, vertice, quantidade_vertices_bancos, tem_ciclo):
    quantidade_vertices_bancos = quantidade_vertices_bancos - 1
    grafo.get_lista_vertices()[vertice].set_cor("cinza")
    
    for adjacente in grafo.get_lista_adjacencia()[vertice]:
        if (not tem_ciclo and adjacente != grafo.get_lista_vertices()[vertice].get_pai()):
            if grafo.get_lista_vertices()[adjacente].get_cor() == "branco":
                grafo.get_lista_vertices()[adjacente].set_pai(vertice)
                (tem_ciclo, quantidade_vertices_bancos) = arvore_auxiliar(grafo, adjacente, quantidade_vertices_bancos, tem_ciclo)
            elif grafo.get_lista_vertices()[adjacente].get_cor() == "cinza":
                tem_ciclo = True
    
    grafo.get_lista_vertices()[vertice].set_cor("preto")
    return (tem_ciclo, quantidade_vertices_bancos)

def arvore(grafo):
    # Atribuicao de branco para as cores e de nulo para os pais de todos os get_lista_vertices
    for i in range(grafo.get_quantidade_vertices()):
        grafo.get_lista_vertices()[i].set_cor("branco")
        grafo.get_lista_vertices()[i].set_pai(None)
    
    # Considera inicialmente que nao existe ciclo
    tem_ciclo = False
    
    # A quantidade inicial de vertices brancos eh o total de vertices do grafo
    quantidade_vertices_bancos = grafo.get_quantidade_vertices()
    
    # Funcao auxiliar que visita todos os vertices conexos
    # Retorna se o grafo possui ciclo e a quantidade de vertices brancos apos a visitacao
    (tem_ciclo, quantidade_vertices_bancos) = arvore_auxiliar(grafo, 0, quantidade_vertices_bancos, tem_ciclo)
    
    # Retorna True se o grafo for uma arvore e False se o grafo nao for uma arvore
    return ((tem_ciclo == False) and (quantidade_vertices_bancos == 0))