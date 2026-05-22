from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete
        

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia < 50:
            return "Distancia abaixo de 50Km"
        else:
            self.frete = self.distancia * self.fator
            return self.frete

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia > 10:
            return "Distancia acima de 10Km"
        else:
            self.frete = self.distancia * self.fator
            return self.frete
