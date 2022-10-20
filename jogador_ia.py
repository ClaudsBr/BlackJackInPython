from jogador import Jogador
from faker import Faker
import random


class JogadorIA(Jogador):

    def __init__(self, ):
        super().__init__(nome=Faker().name())
        self.tendencia = random.choice([1, 2, 3])

    def apostando(self):
        valores_aposta = [
            100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000
        ]
        aposta = random.choice(valores_aposta)
        if aposta > self.get_saldo():
            aposta = self.get_saldo()

        self.set_saldo(self.get_saldo() - aposta)
        self.aposta = aposta
        return aposta

    def jogando(self):
        if self.pontuacao < 15 + self.tendencia:
            return 'p'
        else:
            return 'm'

    def continuando(self):

        if self.get_saldo() == 0:
            print(f"Fim de jogo para o jogador {self.nome} que está sem saldo")
            return 'n'
        else:
            return 's'