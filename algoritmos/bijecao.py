from grafo import Grafo

def bijecao(grafo1, grafo2, vetor_bijecao):
    # Verifica inicialmente se os grafos e a bijecao possuem a mesma quantidade de vertices
    if grafo1.get_quantidade_vertices() == grafo2.get_quantidade_vertices() and grafo1.get_quantidade_vertices() == len(vetor_bijecao):
        for i in range(grafo1.get_quantidade_vertices()):
            for j in range(grafo2.get_quantidade_vertices()):
                # Verifica se a bijecao esta correta
                # Se estiver incorreta, retorna False
                if grafo1.get_matriz_adjacencia()[i][j] != grafo2.get_matriz_adjacencia()[vetor_bijecao[i]][vetor_bijecao[j]]:
                    return False
        
        # Se todas as bijecoes forem corretas, retorna True
        return True
    else:
        # Retorna False se os grafos e a bijecao nao possuirem a mesma quantidade de vertices
        return False

# Funcao principal para teste
def main():
    grafo1 = Grafo(4)
    grafo2 = Grafo(4)
    
    grafo1.adicionar_aresta_nao_direcional(0, 2)
    grafo1.adicionar_aresta_nao_direcional(2, 3)
    grafo1.adicionar_aresta_nao_direcional(3, 1)
    
    grafo2.adicionar_aresta_nao_direcional(2, 1)
    grafo2.adicionar_aresta_nao_direcional(1, 0)
    grafo2.adicionar_aresta_nao_direcional(0, 3)
    
    bijecao1 = [2, 3, 1, 0]
    
    print(bijecao(grafo1, grafo2, bijecao1))
    
if __name__ == "__main__":
    main()
