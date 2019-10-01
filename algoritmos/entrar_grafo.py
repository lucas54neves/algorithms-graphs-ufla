from grafo import Grafo

entrar_grafo():
    quantidade_vertices = int(input("Entre com a quantidade de vertices: "))
    quantidade_arestas = int(input("Entre com a quantidade de arestas: "))
    direcional = int(input("O grafo eh direcional? [0] Nao / [1] Sim "))

    grafo = Grafo(quantidade_vertices)

    for i in range(quantidade_arestas):
        u = int(input("Entre com o vertice u: "))
        v = int(input("Entre com o vertice v: "))
        
        if direcional == 1:
            grafo.adicionar_aresta_direcional(u, v)
        else:
            grafo.adicionar_aresta_nao_direcional(u, v)
    
    return grafo
