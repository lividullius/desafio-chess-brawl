from player import Player
from tournament import Tournament

# [MENU PRINCIPAL]
# Exibe as funcionalidades disponíveis para o usuário
def menu():
    print("\nMenu:")
    print("1 - Cadastrar jogadores")                  # [1] Cadastro de jogadores
    print("2 - Iniciar torneio")                     # [2] Sorteio de partidas e estrutura
    print("3 - Administrar partidas")                # [3] Administração das batalhas
    print("4 - Exibir relatório final")              # [5] Relatório e campeão
    print("5 - Exibir histórico de batalhas")        # [6] Funcionalidade extra
    print("6 - Sair")

# Lista global de jogadores e objeto do torneio
jogadores = []
torneio = None

# LOOP PRINCIPAL
while True:
    menu()
    op = input("Escolha uma opção: ")

    # [1a, 1b] Cadastro de jogadores com validações
    if op == "1":
        n = int(input("Quantos jogadores deseja cadastrar (4 a 8, par)? "))
        if n < 4 or n > 8 or n % 2 != 0:
            print("Número inválido. Deve ser par e entre 4 e 8.")
            continue
        for i in range(n):
            nome = input(f"Nome do jogador {i+1}: ")
            nick = input(f"Nickname do jogador {i+1}: ")
            rank = int(input(f"Ranking (1-15000): "))
            jogadores.append(Player(nome, nick, rank))
        print("Jogadores cadastrados com sucesso!")

    # [2c] Início do torneio com sorteio aleatório das partidas
    elif op == "2":
        if len(jogadores) < 4:
            print("Cadastre os jogadores primeiro!")
            continue
        torneio = Tournament(jogadores)
        torneio.sortear_rodada()
        print("Rodada inicial sorteada!")

    # [3d – 3i + 4j] Administração de partidas e avanço automático de rodada
    elif op == "3":
        if not torneio:
            print("Inicie o torneio primeiro.")
            continue

        pendentes = torneio.partidas_pendentes()
        if not pendentes:
            print("Todas as partidas já foram jogadas.")
            # [4j] Verifica se pode avançar para próxima rodada
            if torneio.todas_rodadas_finalizadas():
                torneio.avancar_fase()
            continue

        # [3d] Seleciona qual partida administrar
        for idx, partida in enumerate(pendentes):
            print(f"{idx+1} - {partida.j1.nickname} vs {partida.j2.nickname}")
        escolha = int(input("Escolha a partida para administrar: ")) - 1
        partida = pendentes[escolha]

        # [3e, 3f] Aplica os eventos para cada jogador manualmente
        for jogador in [partida.j1, partida.j2]:
            print(f"\nEventos para {jogador.nickname}")
            for evento in ['jogada_original', 'gafe', 'posicionamento', 'desrespeito', 'furia']:
                resp = input(f"{evento.replace('_', ' ').title()}? (s/n): ")
                if resp.lower() == "s":
                    partida.registrar_evento(jogador, evento)

        # [3g, 3h, 3i] Calcula vencedor e realiza Blitz Match se necessário
        vencedor = partida.calcular_resultado()
        vencedor.pontos += 30  # bônus do vencedor
        print(f"Vencedor da partida: {vencedor.nickname}")
        partida.finalizada = True
        print("Partida encerrada.")

    # [5k, 5l] Exibe o ranking final com estatísticas e o campeão
    elif op == "4":
        if torneio:
            torneio.mostrar_resultado_final()
            torneio.mostrar_campeao()
        else:
            print("O torneio ainda não foi iniciado.")

    # [6] FEATURE EXTRA – Histórico de batalhas
    elif op == "5":
        if torneio:
            torneio.mostrar_historico()
        else:
            print("O torneio ainda não foi iniciado.")

    # Finaliza o programa
    elif op == "6":
        print("Encerrando o programa.")
        break
