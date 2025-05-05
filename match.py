import random

#representa uma batalha entre dois jogadores
class Match:
    def __init__(self, jogador1, jogador2):
        #jogadores que participam
        self.j1 = jogador1
        self.j2 = jogador2
        #dicionário que guarda quais eventos foram aplicados a cada jogador
        self.eventos_aplicados = {self.j1: set(), self.j2: set()}
        #flag para saber se a partida já foi administrada
        self.finalizada = False

    def registrar_evento(self, jogador, evento):
        #aplica um evento ao jogador, apenas se ele ainda não recebeu esse evento nesta partida
        if evento not in self.eventos_aplicados[jogador]:
            self.eventos_aplicados[jogador].add(evento)
            #mapeamento de eventos com seus respectivos valores
            valores = {
                'jogada_original': 5,
                'gafe': -3,
                'posicionamento': 2,
                'desrespeito': -5,
                'furia': -7
            }
            jogador.pontos += valores[evento]
            jogador.eventos[evento] += 1

    def calcular_resultado(self):
        #verifica pontuação dos jogadores e determina vencedor
        if self.j1.pontos > self.j2.pontos:
            return self.j1
        elif self.j2.pontos > self.j1.pontos:
            return self.j2
        else:
            #se empate, realiza Blitz Match
            return self.blitz_match()

    def blitz_match(self):
        #escolhe aleatoriamente um dos dois jogadores e adiciona +2 pontos
        escolhido = random.choice([self.j1, self.j2])
        escolhido.pontos += 2
        return escolhido
