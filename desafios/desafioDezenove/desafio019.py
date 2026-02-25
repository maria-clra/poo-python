from rich import print

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo= titulo
        self.paginas = paginas

    def avancar_paginas(self):
        return f":book: Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas} páginas[/] no total"


l1 = Livro("10 coisas que aprendi", 20)
print(l1.avancar_paginas())