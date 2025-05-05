from player import Player
from tournament import Tournament

# [MENU PRINCIPAL]
#exibe as funcionalidades disponíveis para o usuário
def menu():
    print("\nMenu:")
    print("1 - Cadastrar jogadores")                  # [1] Cadastro de jogadores
    print("2 - Iniciar torneio")                     # [2] Sorteio de partidas e estrutura
    print("3 - Administrar partidas")                # [3] Administração das batalhas
    print("4 - Exibir relatório final")              # [5] Relatório e campeão
    print("5 - Exibir histórico de batalhas")        # [6] Funcionalidade extra
    print("6 - Sair")

#lista global de jogadores e objeto do torneio
jogadores = []
torneio = None

#LOOP PRINCIPAL
while True:
    menu()
    op = input("Escolha uma opção: ")

    #cadastro de jogadores com validações
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

    #início do torneio com sorteio aleatório das partidas
    elif op == "2":
        if len(jogadores) < 4:
            print("Cadastre os jogadores primeiro!")
            continue
        torneio = Tournament(jogadores)
        torneio.sortear_rodada()
        print("Rodada inicial sorteada!")

    #administração de partidas e avanço automático de rodada
    elif op == "3":
        if not torneio:
            print("Inicie o torneio primeiro.")
            continue

        pendentes = torneio.partidas_pendentes()
        if not pendentes:
            print("Todas as partidas já foram jogadas.")
            #verifica se pode avançar para próxima rodada
            if torneio.todas_rodadas_finalizadas():
                torneio.avancar_fase()
            continue

        #seleciona qual partida administrar
        for idx, partida in enumerate(pendentes):
            print(f"{idx+1} - {partida.j1.nickname} vs {partida.j2.nickname}")
        escolha = int(input("Escolha a partida para administrar: ")) - 1
        partida = pendentes[escolha]

        #aplica os eventos para cada jogador manualmente
        for jogador in [partida.j1, partida.j2]:
    print(f"\nEventos para {jogador.nickname}")
    for evento in ['jogada_original', 'gafe', 'posicionamento', 'desrespeito', 'furia']:
        resp = input(f"{evento.replace('_', ' ').title()}? (s/n): ")
        if resp.lower() == "s":
            partida.registrar_evento(jogador, evento)

        #calcula o vencedor e aplica bônus
        vencedor = partida.calcular_resultado()
        vencedor.pontos += 30
        print(f"Vencedor da partida: {vencedor.nickname}")

        #marca como finalizada
        partida.finalizada = True
        print("Partida encerrada.")

        #verifica se todas as partidas da rodada foram finalizadas
        if torneio.todas_rodadas_finalizadas():
            print("Todas as partidas foram jogadas. Nova fase iniciada!")
            torneio.avancar_fase()

      #exibe o ranking final com estatísticas e o campeão
        elif op == "4":
            if torneio:
                torneio.mostrar_resultado_final()
                torneio.mostrar_campeao()
            else:
                print("O torneio ainda não foi iniciado.")

    #histórico de batalhas
    elif op == "5":
        if torneio:
            torneio.mostrar_historico()
        else:
            print("O torneio ainda não foi iniciado.")

    #finaliza o programa
    elif op == "6":
        print("Encerrando o programa.")
        break
