from rich import print

class Caneta: 

    def __init__(self,cor):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def tampar(self):
        self.tampada = True
          
    def destampar(self):
        self.tampada = False

    def escrever(self, conteudo):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{conteudo}[/]", end="")

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd, end="")

c1 = Caneta("vermelha")
c2 = Caneta("verde")
c3 = Caneta("vermelha")

c3.destampar()
c1.escrever("oi")
c2.escrever("oi")
c3.escrever("oi")

