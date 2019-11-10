#Cria um grafo e popula ele com vértices. Cada vértice terá uma lista com seus vizinhos (adjacentes) e uma lista mostrando de quem eles
#dependem. Um vértice só pode ser visitado após suas dependências terem sido concluídas. Logo a ideia é que deve-se preencher a lista de
#vizinhos e de dependência. Após isso para percorrer basta começar do 0 e olhar os vizinhos dele que é possível percorrer. Para descobrir
#isto é necessário comparar a lista de dependência deste vizinho com o que já foi visitado e então se é possível ir para este vizinho vá 
#para ele coloque-o na lista de visitados marque-o como o atual e chame a função de percorrer novamente.

#Problema na construção da lista de dependência

class Vertice():
    adjacentes = []
    depende_de = []

class Grafo():
    def __init__(self, nome_do_arquivo):
        tamanho = 0
        vertices = []
        
        arquivo = open(nome_do_arquivo , 'r')
            
        tamanho = int(arquivo.readline())

        #Popula o grafo com a quantidade de vértice lida do arquivo
        for x in range(1, tamanho):
            vertices.append(Vertice())
            
        #Verifica se tem mais coisa no arquivo
        linha = arquivo.readline()

            
        #Se tem, e enquanto tiver, irá colocar o vértice da coluna da direita do arquivo como
        #sendo adjacente do vértice da coluna da direita do arquivo. Isto é, o vértice que está
        #na coluna da esquerda será o id para buscar na lista de vértices do grafo após isto
        #irá adicionar à lista de adjacentes deste vértice o vértice da coluna da direita.
        while linha:
            valores_na_linha = linha.split()
                
            #vertice_de_origem = valores_na_linha[0]
            #vertice_de_destino = valores_na_linha[1]
            
            #Cria a lista de adjacentes 
            vertices[int(valores_na_linha[0])].adjacentes.append(int(valores_na_linha[1]))
            
            #Cria a lista dos vértices ao qual ele depende
            if int(valores_na_linha[0]) not in vertices[int(valores_na_linha[1])].depende_de:
                vertices[int(valores_na_linha[1])].depende_de.append(int(valores_na_linha[0]))         
            
            #Debug
            for x in range(0,9):
                print('Lista de quem o vértice {} é vizinho'.format(int(valores_na_linha[x])), vertices[x].adjacentes)
                
            #Checa a próxima linha e segue o while
            linha = arquivo.readline()
            
        
def percorre(grafo):

    #Verifica qual dos vizinhos podem ser acessados com base no que já foi visitado
    for vizinho in grafo.vertices[atual].adjacentes:
            
        #Se já visitamos todos os vértices necessários para o vértice atual
        if visitado in grafo.vertices[vizinho].depende_de:
            atual = vizinho
                
            #Adiciona o vértice atual aos visitados
            visitado.append(grafo.vertices[atual])
               
            percorre(grafo)
    

        
grafo = Grafo("Ex2.txt")
visitado = []
atual = 0
percorre(grafo)
print(visitado)
    
