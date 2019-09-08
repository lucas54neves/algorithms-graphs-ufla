class Vertice:
    def __init__(self, x):
        self.id = x
        self.cor = "branco"
        self.distancia = float("inf")
        self.predecessor = None
        self.f = float("inf")
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    
    def set_distancia(self, nova_distancia):
        self.distancia = nova_distancia
    
    def set_predecessor(self, novo_predecessor):
        self.predecessor = novo_predecessor
    
    def set_f(self, novo_f):
        self.f = novo_f
    
    def get_id(self):
        return self.id
    
    def get_cor(self):
        return self.cor
    
    def get_distancia(self):
        return self.distancia
    
    def get_predecessor(self):
        return self.predecessor
    
    def get_f(self):
        return self.f
