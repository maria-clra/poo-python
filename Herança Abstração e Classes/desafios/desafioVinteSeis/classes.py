from abc import ABC, abstractmethod
from rich import print, inspect
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.sal_bruto = salario
        self.sal_liquido = salario
        self.sal_min = 1612.00
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        analise = self.sal_bruto / self.sal_min
        conteudo = f"O salário de {self.nome} ({type(self).__name__}) é de {self.sal_bruto:.2f}\n"
        conteudo += f"e corresponde a {analise:.1f} salários mínimos"
        resultado = Panel(conteudo, title="Análise de Salário",width=50)
        print(resultado)

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):

        salario = valor_hora * horas_trab

        super().__init__(nome, salario)

        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.sal_liquido = self.sal_bruto
        return self.sal_liquido

class Mensalista(Funcionario):
    def calc_sal(self):
        desconto = self.sal_bruto * (self.inss / 100)

        self.sal_liquido = self.sal_bruto - desconto

        return self.sal_liquido