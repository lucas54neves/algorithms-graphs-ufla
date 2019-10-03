class Vertice:
    def __init__(self, i):
        self.indice = i
        self.cor = "branco"
        self.pai = None
        self.tempo_inicial = -1
        self.tempo_final = -1
    
    def get_indice(self):
        return self.indice
    
    def get_cor(self):
        return self.cor
    
    def get_pai(self):
        return self.pai
    
    def get_tempo_inicial(self):
        return self.tempo_inicial
    
    def get_tempo_final(self):
        return self.tempo_final
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    
    def set_pai(self, novo_pai):
        self.pai = novo_pai
    
    def set_tempo_inicial(self, novo_tempo):
        self.tempo_inicial = novo_tempo
    
    def set_tempo_final(self, novo_tempo):
        self.tempo_final = novo_tempo 
