from rich.panel import Panel
from rich import inspect
from rich import print

class Churrasco:
    carne:float = 0.400
    kg:float = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def quant_carne(self) -> float:
        return self.quant * Churrasco.carne
    
    def custo_total(self) -> float:
        return self.quant_carne() * self.__class__.kg
    
    def custo_individual(self) -> float:
        return self.custo_total() / self.quant
        #Consumo padrão: 400g por pessoa
        #Preço: 82,40/Kg
   
        comprar = Churrasco.carne * self.quant
        total = Churrasco.kg * comprar
        valorPessoa = total / self.quant
    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n"
        conteudo += f"Cada participante comerá {Churrasco.carne}Kg e cada Kg custa R${Churrasco.kg:.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.quant_carne()}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${self.custo_total():,.2f}[/] \n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.custo_individual():,.2f}[/] para participar"

        print(Panel(conteudo, title="Churras dos Amigos"))
  
c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()