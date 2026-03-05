from rich import print

class Livro:

    def __init__(self, titulo, paginas_total):
        self.titulo= titulo
        self.paginas_total = paginas_total
        self.pagina_atual = 0
        print (f":book: Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas_total} páginas[/] no total.")
    
    def avancar_paginas(self, paginas):
        if self.pagina_atual + paginas <= self.paginas_total:
            self.pagina_atual += paginas
            print(f"Você avaçou {paginas} páginas e agora está na página {self.pagina_atual}") 
        
        else:
            self.pagina_atual = self.paginas_total
            print(f":rotating_light: Você chegou ao final do livro {self.titulo}")
        
        
        
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(5)