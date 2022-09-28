from jogador import Jogador
from faker import Faker
import random

class JogadorIA(Jogador):

    def __init__(self, ):
        super().__init__(nome=Faker().name())
        self.bias = random.choice([1, 2, 3])

    def apostando(self):
        valores_aposta = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        aposta = random.choice(valores_aposta)
        self.saldo -= aposta
        self.aposta = aposta
        return aposta

    def jogando(self):
        if self.valores < 15 + self.bias:
            return 'p'
        else:
            return 'm'