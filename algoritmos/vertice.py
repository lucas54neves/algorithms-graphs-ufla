class Vertice:
    def __init__(self, i):
        self.indice = i
        self.cor = "branco"
        self.pai = None
        self.tempo_inicial = -1
        self.tempo_final = -1
        self.distancia = float("inf")
        # O menor número de pré-ordem que pode ser alcançado por v utilizando
        # arcos da arborescência e até um arco de retorno
        self.low = float("inf")

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

    def get_distancia(self):
        return self.distancia

    def get_low(self):
        return self.low

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def set_pai(self, novo_pai):
        self.pai = novo_pai

    def set_tempo_inicial(self, novo_tempo):
        self.tempo_inicial = novo_tempo

    def set_tempo_final(self, novo_tempo):
        self.tempo_final = novo_tempo

    def set_distancia(self, nova_distancia):
        self.distancia = nova_distancia

    def set_low(self, novo_low):
        self.low = novo_low
