from grafo import *

def ponte(grafo):
    for i in range(grafo.get_quantidade_vertices()):
        if grafo.get_lista_vertices()[i].get_visitado() == False:
            ponte_auxiliar(grafo, i)

def ponte_auxiliar(grafo, vertice):
    grafo.get_lista_vertices()[vertice].set_visitado(True)
    grafo.get_lista_vertices()[vertice].set_tempo(grafo.get_tempo())
    grafo.get_lista_vertices()[vertice].set_low(grafo.get_tempo())
    grafo.set_tempo(grafo.get_tempo()+1)

    for adjacente in grafo.get_lista_adjacencia()[vertice]:
        if grafo.get_lista_vertices()[adjacente].get_visitado() == False:
            grafo.get_lista_vertices()[adjacente].set_pai(vertice)
            ponte_auxiliar(grafo, adjacente)

            grafo.get_lista_vertices()[vertice].set_low(min(grafo.get_lista_vertices()[vertice].get_low(), grafo.get_lista_vertices()[adjacente].get_low()))

            if grafo.get_lista_vertices()[adjacente].get_low() > grafo.get_lista_vertices()[vertice].get_tempo():
                print("A aresta {} - {} eh ponte".format(vertice, adjacente))

        elif adjacente != grafo.get_lista_vertices()[vertice].get_pai():
            grafo.get_lista_vertices()[vertice].set_low(min(grafo.get_lista_vertices()[vertice].get_low(), grafo.get_lista_vertices()[adjacente].get_tempo()))
            if grafo.get_lista_vertices()[vertice].get_tempo() > grafo.get_lista_vertices()[adjacente].get_tempo():
                grafo.set_caminho(vertice+1, adjacente+1)
