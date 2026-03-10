from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.itens = []

    def add_favoritos(self, jogos_favoritos):
        self.itens.append(jogos_favoritos)
        return self.itens

    def ficha_gamer(self):
        title = f"Jogador < {self.nick} >"
        conteudo = f"Nome real: {self.nome}\n"
        conteudo += "Jogos favoritos:\n"
        conteudo += ":video_game: " + "\n:video_game: ".join(self.itens)
        ficha = Panel(conteudo, title=title)
        print(ficha)



j1 = Gamer("Maria", "maclaranb")
j1.add_favoritos("War")
j1.add_favoritos("Wer")
j1.add_favoritos("Wir")
j1.ficha_gamer()
        