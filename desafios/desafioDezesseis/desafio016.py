from rich import print
from rich import inspect

class Funcionario:
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou {self.nome}, e sou {self.cargo} do setor {self.setor} da empresa {self.__class__.empresa}."
    

c1 = Funcionario("Maria", "Administação", "Diretora")
c2 = Funcionario("Diego", "Engenharia", "Desenhista")
print(c1.apresentacao())
print(c2.apresentacao())