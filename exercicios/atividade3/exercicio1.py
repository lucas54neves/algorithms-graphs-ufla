def leitura(nome_arquivo):
    arquivo = open(nome_arquivo, "r")

    #numero_vertices = int(arquivo.readline())

    #grafo = Grafo(numero_vertices)

    for linha in arquivo:
        valores = linha.split()
        #grafo.adicionar_aresta(int(valores[0]), int(valores[1]))

        # Testa se os valores foram lidos
        print(valores)

leitura("Ex1.txt")
