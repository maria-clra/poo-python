from rich import print

class Livro:

    def __init__(self, titulo, paginas_total):
        self.titulo= titulo
        self.paginas_total = paginas_total
        self.pagina_atual = 1
        print (f":book: Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas_total} páginas[/] no total.")
    
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward: ", end=' ')
                cont +=1 
        print(f"[blue]Você avançou {cont} páginas e agora está na página {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: Você chegou ao fim do livro {self.titulo}.")
    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.paginas_total:
            return True
        else: 
            return False
        
        
        
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(5)
l1.avancar_paginas(10)