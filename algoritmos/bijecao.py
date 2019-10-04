from grafo import *

def bijecao(grafo1, grafo2, vetor_bijecao):
    for i in range(grafo1.get_quantidade_vertices()):
        for j in range(grafo2.get_quantidade_vertices()):
            if grafo1.get_matriz_adjacencia()[i][j] != grafo2.get_matriz_adjacencia()[vetor_bijecao[i]][vetor_bijecao[j]]:
                return False
    return True

# Funcao principal para teste
def main():
    grafo1 = Grafo(4)
    grafo2 = Grafo(4)
    grafo3 = Grafo(4)

    grafo1.adicionar_aresta_nao_direcional(0, 1)
    grafo1.adicionar_aresta_nao_direcional(1, 2)
    grafo1.adicionar_aresta_nao_direcional(2, 3)

    grafo2.adicionar_aresta_nao_direcional(0, 2)
    grafo2.adicionar_aresta_nao_direcional(1, 0)
    grafo2.adicionar_aresta_nao_direcional(1, 2)
    grafo2.adicionar_aresta_nao_direcional(2, 3)

    grafo3.adicionar_aresta_nao_direcional(0, 2)
    grafo3.adicionar_aresta_nao_direcional(1, 0)
    grafo3.adicionar_aresta_nao_direcional(2, 3)

    bijecao1 = [1, 0, 2, 3]
    print(bijecao(grafo1, grafo2, bijecao1))

    bijecao2 = [1, 0, 2, 3]
    print(bijecao(grafo1, grafo3, bijecao2))

if __name__ == "__main__":
    main()
