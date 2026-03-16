from rich import print

class Caneta: 
    tampada = True

    def __init__(self,cor):
        self.cor = cor

    def tampar(self):
        self.tampada = True
          
    def destampar(self):
        self.tampada = False

    def escrever(self, conteudo):
        if not self.tampada:
            if self.cor == "vermelha":
                print(f"[red]{conteudo}")
            elif self.cor == "verde":
                print(f"[green]{conteudo}")
            elif self.cor == "azul":
                print(f"[blue]{conteudo}")

    def quebrar_linha(self):
        print("\n")

c1 = Caneta("vermelha")
c2 = Caneta("verde")
c3 = Caneta("vermelha")

c2.destampar()
c2.escrever("oi")
c3.escrever("sei")
c3.tampar()
c3.escrever("oi")
c3.escrever("sei")
