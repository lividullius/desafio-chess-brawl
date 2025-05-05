# Desafio-Chess-Brawl
Este projeto simula um torneio de xadrez alternativo chamado **Chess Brawl**, em que jogadores disputam em rodadas eliminatórias com influência de eventos especiais. A administração do torneio é feita manualmente, com pontuação ajustada conforme o desempenho dos jogadores durante as partidas. Desenvolvido por Lívia Nöer.

O desafio propõe a criação de um sistema para:

- Cadastrar jogadores com nome, nickname e pontuação de ranking.
- Sortear partidas em rodadas eliminatórias.
- Simular eventos durante batalhas que afetam a pontuação.
- Identificar o vencedor de cada partida e da competição.
- Exibir relatórios e histórico das batalhas.

Funcionalidades disponíveis

[1] Cadastro de jogadores
Entrada de nome, nickname e ranking.
Validação: de 4 a 8 jogadores, número par.

[2] Início do torneio
Sorteio aleatório das partidas.
Inicialização da estrutura do torneio.

[3] Administração das partidas
Seleção de partidas pendentes.
Registro de eventos manuais:
Jogada original (+5)
Gafe (-3)
Posicionamento vantajoso (+2)
Desrespeito (-5)
Fúria (-7)
Cálculo automático do vencedor.
Blitz Match automático em caso de empate.
Bônus de +30 pontos para o vencedor.
Avanço automático de fase ao final da rodada.

[4] Exibição do relatório final
Lista dos jogadores ordenados por pontuação final.
Estatísticas individuais de eventos.
Apresentação do campeão.

[5] Histórico de batalhas
Exibe as partidas realizadas e os vencedores.

[6] Sair
Encerra o programa.
