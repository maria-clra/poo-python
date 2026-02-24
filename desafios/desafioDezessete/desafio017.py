from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def etiqueta(self):
        etiqueta = ("Produto", {self.produto}, ("-----------------"), ".....", {self.preco}, ".....")
        print(etiqueta)

    def etiqueta2(self):
        etiqueta2 = (Panel(title="Produto", {self.produto}, subtitle=("-----------------"), ".....", {self.preco}, "....."))
        print(etiqueta2)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8.000)
p1.etiqueta()
p2.etiqueta()
p1.etiqueta2()
p2.etiqueta2()
