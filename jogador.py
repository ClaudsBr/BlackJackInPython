from random import random
from config import SALDO_INICIAL_JOGADOR
from uuid import uuid4

from faker import Faker


class Jogador:
    def __init__(self, nome=Faker().name()):
        self.nome = nome
        self.saldo = SALDO_INICIAL_JOGADOR
        self.cartas = []
        self.aposta = 0
        self.valores = 0
        self.id = str(uuid4())

    def jogador_ganha(self, aposta):
        self.saldo += 2 * aposta

    def __str__(self):
        string_de_retorno = f"Jogador: {self.nome}\n"
        for carta in self.cartas:
            string_de_retorno += f'{carta}\n'
        string_de_retorno += f'Mão: {self.valores}\nSaldo: {self.saldo}'
        return string_de_retorno

    def jogando(self):
        pergunta = input("Digite P para pedir outra carta ou M para manter suas cartas atuais\n")
        return pergunta[0].lower()

    def apostando(self):
        while True:
            try:
                aposta = int(input(f"Digite o valor da sua aposta {self.nome}\n"))
            except ValueError:
                print("Valor não aceito")
            else:
                if (self.saldo < aposta) or (aposta < 0):
                    print("Aposta Inválida")
                else:
                    self.saldo -= aposta
                    self.aposta = aposta
                    return aposta
