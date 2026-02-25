from rich.panel import Panel
from rich import inspect
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        #Consumo padrão: 400g por pessoa
        #Preço: 82,40/Kg
        
        carne = 0.4
        kg = 82.40
        comprar = carne * self.quant
        total = kg * comprar
        valorPessoa = total % self.quant

        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n"
        conteudo += f"Cada participante comerá {carne}Kg e cada Kg custa R${kg:.2f}\n"
        conteudo += f"Recomendo [blue]comprar {comprar}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${total:.2f}[/] \n"
        conteudo += f"Cada pessoa pagará [yellow]R${valorPessoa:.2f}[/] para participar"

        print(Panel(conteudo, title="Churras dos Amigos"))
  
c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()