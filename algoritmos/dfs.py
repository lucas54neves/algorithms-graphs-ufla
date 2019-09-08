
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
        if grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i]].get_cor() == "branco":
            grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i]].set_predecessor(grafo.get_lista_vertices()[id_vertice].get_id())
            dfsVisit(grafo, grafo.get_lista_vertices()[grafo.get_lista_adj()[id_vertice][i]].get_id())
    
    grafo.get_lista_vertices()[id_vertice].set_cor("preto")
    tempo = tempo + 1
    grafo.get_lista_vertices()[id_vertice].set_f(tempo)
