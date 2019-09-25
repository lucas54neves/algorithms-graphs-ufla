class Grafo:
    def __init__(self, n):
        # Quantidade de vertices
        self.quantidade_vertices = n

        # Lista de vertices para realizar as operacoes
        self.lista_vertices = []
        for i in range(n):
            self.lista_vertices.append(self.Vertice(i))

        # Lista de adjacencia
        self.lista_adjacencia = []
        for i in range(n):
            self.lista_adjacencia.append([])
        
        # Matriz de adjacencia
        self.matriz_adjacencia = []
        # Inicializa linhas
        linha = []
        for i in range(n):
            linha.append(0)
        for i in range(n):
            self.matriz_adjacencia.append(linha)
    
    # Retorna a quantidade vertices
    def get_quantidade_vertices(self):
        return self.quantidade_vertices

    # Retorna a lista de vertices
    def get_lista_vertices(self):
        return self.lista_vertices

    # Retorna a lista de adjacencia
    def get_lista_adjacencia(self):
        return self.lista_adjacencia
    
    # Retorna a matriz de adjacencia
    def get_matriz_adjacencia(self):
        return self.matriz_adjacencia

    # Adiciona aresta direcional
    def adicionar_aresta_direcional(self, u, v):
        # Adicionando na lista de adjacencia
        self.lista_adjacencia[u].append(v)
        
        # Adicionando na matriz de adjacencia
        self.matriz_adjacencia[u][v] = 1
        
    # Adiciona aresta nao direcinal
    def adicionar_aresta_nao_direcional(self, u, v):
        # Adicionando na lista de adjacencia
        self.lista_adjacencia[u].append(v)
        self.lista_adjacencia[v].append(u)
        
        # Adicionando na matriz de adjacencia
        self.matriz_adjacencia[u][v] = 1
        self.matriz_adjacencia[v][u] = 1
    
    # Exibe a lista de adjacencia
    def exibir_lista_adjacencia(self):
        for i in range(self.quantidade_vertices):
            lista = []
            for j in range(len(self.lista_adjacencia[i])):
                lista.append(self.get_lista_adjacencia()[i][j])
            print(lista)
            
    # Exibe a matriz de adjacencia
    def exibir_matriz_adjacencia(self):
        for i in range(self.quantidade_vertices):
            lista = []
            for j in range(self.quantidade_vertices):
                lista.append(self.get_matriz_adjacencia()[i][j])
            print(lista)
    
    class Vertice:
        def __init__(self, x):
            self.indice = x
            self.cor = "branco"
            self.distancia = float("inf")
            self.pai = None
            self.tempo_inicial = float("inf")
            self.tempo_final = float("inf")
        
        def set_cor(self, nova_cor):
            self.cor = nova_cor
        
        def set_distancia(self, nova_distancia):
            self.distancia = nova_distancia
        
        def set_pai(self, padrasto):
            self.pai = padrasto
        
        def set_tempo_inicial(self, novo_inicial):
            self.tempo_inicial = novo_inicial
        
        def set_tempo_final(self, novo_final):
            self.tempo_final = novo_final
        
        def get_indice(self):
            return self.indice
        
        def get_cor(self):
            return self.cor
        
        def get_distancia(self):
            return self.distancia
        
        def get_pai(self):
            return self.pai
        
        def get_tempo_inicial(self):
            return self.tempo_inicial
        
        def get_tempo_final(self):
            return self.tempo_final
