from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo, empresa = "Curso em Video"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        print(f":yellow_heart: Olá, sou {self.nome}, e sou {self.cargo} no setor {self.setor} da empresa {self.empresa}.")


c1 = Funcionario("Maria", "Administação", "Diretora")
c2 = Funcionario("Diego", "Engenharia", "Desenhista")
print(c1.apresentacao())
print(c2.apresentacao())