class Player:
    def __init__(self, nome, nickname, ranking):
        self.nome = nome
        self.nickname = nickname
        self.ranking = ranking
        self.pontos = 70
        self.estatisticas = {
            'jogada_original': 0,
            'gafe': 0,
            'posicionamento': 0,
            'desrespeito': 0,
            'furia': 0
        }

    def __str__(self):
        return f"{self.nome} ({self.nickname}) - {self.pontos} pontos"
        