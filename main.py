from player import Player
from tournament import Tournament

def cadastrar_jogadores():
    jogadores = []
    print("Cadastro de jogadores:")
    while True:
        nome = input("Nome: ")
        nickname = input("Nickname: ")
        try:
            ranking = int(input("Ranking (1 a 15000): "))
            if not (1 <= ranking <= 15000):
                raise ValueError("Ranking fora do intervalo permitido.")
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            continue

        jogadores.append(Player(nome, nickname, ranking))

        if len(jogadores) >= 4 and len(jogadores) % 2 == 0:
            continuar = input("Deseja adicionar mais jogadores? (s/n): ").lower()
            if continuar == 'n' or len(jogadores) == 8:
                break
            elif continuar != 's':
                print("Entrada inválida, esperando 's' ou 'n'.")

def menu_batalhas(torneio):
    while not torneio.todas_partidas_concluidas():
        for i, partida in enumerate(torneio.rodada_atual):
            if not partida.finalizada:
                print(f"\nPartida {i+1}: {partida.jogador1} vs {partida.jogador2}")
                for jogador in [partida.jogador1, partida.jogador2]:
                    print(f"\nEventos para {jogador.nickname}:")
                    for evento in ['jogada_original', 'gafe', 'posicionamento', 'desrespeito', 'furia']:
                        usar = input(f"{evento.replace('_', ' ').title()}? (s/n): ").lower()
                        if usar == 's':
                            partida.aplicar_evento(jogador, evento)
                partida.resolver_partida()
                print(f" Vencedor: {partida.vencedor.nickname}")

def relatorio_final(torneio):
    print("\n RESULTADO FINAL")
    ranking = torneio.ranking_final()
    for p in ranking:
        print(f"{p.nickname} - Pontos: {p.pontos} | Estatísticas: {p.estatisticas}")
    print(f"\n CAMPEÃO: {torneio.campeao.nome} ({torneio.campeao.nickname})")

def main():
    jogadores = cadastrar_jogadores()
    torneio = Tournament(jogadores)
    torneio.sortear_partidas()

    while not torneio.campeao:
        menu_batalhas(torneio)
        torneio.avancar_fase()

    relatorio_final(torneio)

if __name__ == "__main__":
    main()