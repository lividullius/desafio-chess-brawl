#classe que representa o jogador
class Player: 
    def __init__(self, nome, nickname, ranking): 
        #nome real do jogador
        self.nome = nome 
        #apelido usado no jogo
        self.nickname = nickname
        #ranking do jogador
        self.ranking = ranking 
        #ponto no torneio (todos começam com 70)
        self.pontos = 70 
        #dicionário para contar os eventos recebidos ao longo do torneio
        self.eventos = {
            'jogada_original': 0,
            'gafe': 0,
            'posicionamento': 0,
            'desrespeito': 0,
            'furia': 0
        }

    def __str__(self):
        return f"{self.nome} ({self.nickname}) - {self.pontos} pontos"
        
