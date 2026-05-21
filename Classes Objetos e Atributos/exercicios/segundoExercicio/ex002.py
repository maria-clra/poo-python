class Gafanhoto:

    """Essa classe cria um Garfanhoto, que é uma pessoa que tem nome e idade.

    """
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1 
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    
    
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)