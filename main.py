from player import Player
from tournament import Tournament

#função que exibe o menu principal
def menu():
    print("\nMenu:")
    print("1 - Cadastrar jogadores")
    print("2 - Iniciar torneio")
    print("3 - Administrar partidas")
    print("4 - Exibir relatório final")
    print("5 - Exibir histórico de batalhas")
    print("6 - Sair")

#lista para armazenar jogadores
jogadores = []
torneio = None

while True:
    menu()
    op = input("Escolha uma opção: ")

    if op == "1":
        #cadastro de jogadores com validação
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

    elif op == "2":
        #início do torneio
        if len(jogadores) < 4:
            print("Cadastre os jogadores primeiro!")
            continue
        torneio = Tournament(jogadores)
        torneio.sortear_rodada()
        print("Rodada inicial sorteada!")

    elif op == "3":
        #administração de batalhas
        if not torneio:
            print("Inicie o torneio primeiro.")
            continue
        pendentes = torneio.partidas_pendentes()
        if not pendentes:
            print("Todas as partidas já foram jogadas.")
            if torneio.todas_rodadas_finalizadas():
                torneio.avancar_fase()
            continue

        #listar partidas disponíveis
        for idx, partida in enumerate(pendentes):
            print(f"{idx+1} - {partida.j1.nickname} vs {partida.j2.nickname}")
        escolha = int(input("Escolha a partida para administrar: ")) - 1
        partida = pendentes[escolha]

        #aplicar eventos manualmente a cada jogador
        for jogador in [partida.j1, partida.j2]:
            print(f"\nEventos para {jogador.nickname}")
            for evento in ['jogada_original', 'gafe', 'posicionamento', 'desrespeito', 'furia']:
                resp = input(f"{evento.replace('_', ' ').title()}? (s/n): ")
                if resp.lower() == "s":
                    partida.registrar_evento(jogador, evento)

        partida.finalizada = True
        print("Partida encerrada.")

    elif op == "4":
        if torneio:
            torneio.mostrar_resultado_final()
            torneio.mostrar_campeao()
        else:
            print("O torneio ainda não foi iniciado.")

    elif op == "5":
        if torneio:
            torneio.mostrar_historico()
        else:
            print("O torneio ainda não foi iniciado.")

    elif op == "6":
        print("Encerrando o programa.")
        break
