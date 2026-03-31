from rich.panel import Panel
from rich import print

class ControleRemoto:
    canal_minimo = 1
    canal_maximo = 6
    volume_minimo = 1
    volume_maximo = 5

    def __init__(self, canal=1, volume=2):
        self.canal_atual = canal 
        self.volume_atual = volume
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_maximo:
                self.canal_atual = ControleRemoto.canal_minimo
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_minimo:
                self.canal_atual = ControleRemoto.canal_maximo
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_maximo:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_minimo:
                self.volume_atual -= 1

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = f":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_minimo, ControleRemoto.canal_maximo + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f"{canal}"

            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_minimo, ControleRemoto.volume_maximo + 1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"


        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)


c1 = ControleRemoto()
while True:
    c1.mostrar_tv()
    comando = str(input(f" < CH >  - VOL  + "))
    match comando:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '>':
            c1.canal_mais()
        case '>':
            c1.canal_menos()
        case '-':
            c1.volume_menos()
        case '+':
            c1.volume_mais()
print("\n * 10")

