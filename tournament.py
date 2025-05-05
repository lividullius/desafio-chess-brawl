import random
from match import Match

#gerencia o andamento do torneio, rodadas e histórico
class Tournament:
    def __init__(self, jogadores):
        #lista de todos os jogadores inscritos
        self.jogadores = jogadores
        #lista de rodadas (cada uma com partidas)
        self.rodadas = []
        #lista com resumo das partidas jogadas
        self.historico = []

    def sortear_rodada(self):
        #embaralha jogadores e agrupa em pares para criar partidas
        random.shuffle(self.jogadores)
        rodada = []
        for i in range(0, len(self.jogadores), 2):
            partida = Match(self.jogadores[i], self.jogadores[i+1])
            rodada.append(partida)
        self.rodadas.append(rodada)

    def partidas_pendentes(self):
        #retorna todas as partidas que ainda não foram finalizadas
        return [m for m in self.rodadas[-1] if not m.finalizada]

    def avancar_fase(self):
        #coleta vencedores das partidas e cria nova rodada
        vencedores = []
        for match in self.rodadas[-1]:
            vencedor = match.calcular_resultado()
            vencedor.pontos += 30  #bônus por vencer
            vencedores.append(vencedor)
            self.historico.append((match.j1.nickname, match.j2.nickname, vencedor.nickname))
        self.jogadores = vencedores
        if len(vencedores) > 1:
            self.sortear_rodada()

    def todas_rodadas_finalizadas(self):
        #verifica se todas as partidas da rodada atual já foram administradas
        return all(m.finalizada for m in self.rodadas[-1])

    def mostrar_resultado_final(self):
        #exibe ranking final dos jogadores com estatísticas
        print("\nRanking Final:")
        todos = sorted(self.jogadores, key=lambda j: j.pontos, reverse=True)
        for j in todos:
            print(f"{j.nickname} - {j.pontos} pontos")
            for evento, qtd in j.eventos.items():
                print(f"  {evento}: {qtd}")

    def mostrar_campeao(self):
        #exibe o campeão (único restante)
        if len(self.jogadores) == 1:
            campeao = self.jogadores[0]
            print(f"\n Campeão: {campeao.nome} ({campeao.nickname}) com {campeao.pontos} pontos!")

    def mostrar_historico(self):
        #exibe o histórico resumido de partidas
        print("\n Histórico de batalhas:")
        for j1, j2, vencedor in self.historico:
            print(f"{j1} vs {j2} → Vencedor: {vencedor}")

         
