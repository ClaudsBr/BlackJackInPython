import random
from constantes import PAUS, COPAS, OUROS, ESPADAS, REI, AS, DAMA, VALETE
from jogador import Jogador
from uuid import uuid4


class Baralho():

    def __init__(self):

        self.cartas = []

        for naipe in [PAUS, COPAS, ESPADAS, OUROS]:
            for numero in range(2, 11):
                carta = {
                    "naipe": naipe,
                    "numero": str(numero),
                    "jogador": None,
                    "id": str(uuid4())
                }
                self.cartas.append(carta)

            for numero in [AS, DAMA, VALETE, REI]:
                carta = {
                    "naipe": naipe,
                    "numero": numero,
                    "jogador": None,
                    "id": str(uuid4())
                }
                self.cartas.append(carta)
        self.embaralha()
        self.__index_generator = 0

    def dar_as_cartas(self, jogador: Jogador):

        return [self.pedir_carta(jogador), self.pedir_carta(jogador)]

    def pedir_carta(self, jogador: Jogador):
        carta = self.cartas[self.__index_generator]
        carta['jogador'] = jogador.nome
        jogador.cartas.append(carta)
        self.__index_generator += 1
        return carta

    def embaralha(self):
        return random.shuffle(self.cartas)

    @staticmethod
    def somar_pontos(cartas):
        soma = 0
        valores = []
        for carta in cartas:
            if (carta["numero"] == REI) \
                    or (carta["numero"] == DAMA) \
                    or (carta["numero"] == VALETE):
                soma += 10
                valores.append(carta['numero'])
            elif carta["numero"] == AS:
                soma += 1
                valores.append(carta['numero'])
            else:
                soma += int(carta['numero'])
                valores.append(int(carta['numero']))

        if AS in valores:
            if (REI in valores) \
                    or (DAMA in valores) \
                    or (VALETE in valores):
                soma += 10
                if soma > 21:
                    soma -= 10
        return soma

    def exibir_cartas(self):
        for carta in self.cartas:
            print(f"{carta['numero']} {carta['naipe']}")
