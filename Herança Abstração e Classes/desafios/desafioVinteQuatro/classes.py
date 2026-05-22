from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print("--- Bebida Pronta ---")

    def ferver_agua(self):
        return "1 - Fervendo a água a 100 graus Celsius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        return "2 - Passando água pressurizada pelo pó de café moído."

    def servir(self):
        return "3 - Servindo em xícara pequena."


class Leite(BebidaQuente):

    def misturar(self):
        return "2 - Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "3 - Servindo na caneca grande, já com café."


class Cha(BebidaQuente):

    def misturar(self):
        return "2 - Mergulhando o sachê de ervas na água."

    def servir(self):
        return "3 - Servindo na caneca de porcelana com limão."