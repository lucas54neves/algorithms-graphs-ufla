'''
Resposta em Python
GCC218 - 2019/02
Atividade: 
Grupo:
    Lucas Neves, 14A, 201720357
    Davi Horner, 10A
    Thiago Luigi, 10A
Data: 06/09/2019  
'''

class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0

def leGrafo():
    arquivo = open('ativ1_instance.txt', 'r')
    
    # Le do arquivo a quantidade de vertices
    # Sendo n a quantidade de vertices
    linha = arquivo.readline()
    n = int(linha)
    
    # Cria a lista de adjacencia
    lista = []
    for i in range(n):
        lista.append([])
    
    # Le todos os vertices adjacentes e guarda na lista
    linha = arquivo.readline()
    while linha:
        valores = linha.split()
        
        # Pega o vertice que vai ser a posicao na lista
        # Os vertices seguintes sao adjacentes a esse vertice
        vertice = int(valores.pop(0))
        
        while valores != []:
            adjacente = valores.pop(0)
            if adjacente != '-':
                lista[vertice].append(int(adjacente))
        
        linha = arquivo.readline()
    
    print(lista)
    
## Imprime os vertices dominantes usando DFS
#def abordagem1(n, Adj, r):
    ##cor = []
    ##for i in range n:
        ##cor.append("branco")
    ##cor[r] = cinza
    ##p = Pilha()
    ##p.empilha(r)
    ##while not p.vazia():
        ##u = p.desempilha()
        ##v = # proximo(Adj[u]
        ##if v != nil:
            ##if cor[v] == branco:
                ##cor[v] = cinza
                ##p.empilha(v)
            ##else:
                ##p.desempilha()
    

## Imprime os vertices dominantes usando BFS
#def abordagem2():
    

#abordagem1()
#abordagem2()


arquivo = open('ativ1_instance.txt', 'r')
    
leGrafo()
