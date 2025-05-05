import random

EVENTOS = {
    'jogada_original': 5,
    'gafe': -3,
    'posicionamento': 2,
    'desrespeito': -5,
    'furia': -7
}

class Match:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.eventos_aplicados = {jogador1.nickname: [], jogador2.nickname: []}
        self.finalizada = False
        self.vencedor = None

    def aplicar_evento(self, jogador, evento):
        if evento not in self.eventos_aplicados[jogador.nickname]:
            jogador.pontos += EVENTOS[evento]
            jogador.estatisticas[evento] += 1
            self.eventos_aplicados[jogador.nickname].append(evento)

    def resolver_partida(self):
        if self.jogador1.pontos == self.jogador2.pontos:
            escolhido = random.choice([self.jogador1, self.jogador2])
            escolhido.pontos += 2
            print(f"⚡ Blitz Match! {escolhido.nickname} ganhou 2 pontos.")

        self.vencedor = self.jogador1 if self.jogador1.pontos > self.jogador2.pontos else self.jogador2
        self.vencedor.pontos += 30
        self.finalizada = True
