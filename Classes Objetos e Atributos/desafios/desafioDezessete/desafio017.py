from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco
    

    def etiqueta(self):
        conteudo = f"{self.produto.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        preco = f"{self.preco:,.2f}"
        conteudo += f"{preco.center(30, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)
        
p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p1.etiqueta()

p2 = Produto("Notebook Gamer", 8.000)
p2.etiqueta()