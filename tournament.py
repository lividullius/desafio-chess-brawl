import random
from match import Match

class Tournament:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.rodadas = []
        self.rodada_atual = []
        self.campeao = None

    def sortear_partidas(self):
        random.shuffle(self.jogadores)
        self.rodada_atual = [Match(self.jogadores[i], self.jogadores[i+1]) for i in range(0, len(self.jogadores), 2)]
        self.rodadas.append(self.rodada_atual)

    def todas_partidas_concluidas(self):
        return all(m.finalizada for m in self.rodada_atual)

    def avancar_fase(self):
        vencedores = [m.vencedor for m in self.rodada_atual]
        if len(vencedores) == 1:
            self.campeao = vencedores[0]
        else:
            self.jogadores = vencedores
            self.sortear_partidas()

    def ranking_final(self):
        return sorted(self.jogadores, key=lambda x: x.pontos, reverse=True)
