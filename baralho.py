import random
from player import Player


class Baralho():

    def __init__(self):
        self.cartas = []
        for naipe in ["Paus", "Copas", "Espadas", "Ouros"]:
            for numero in range(1, 11):
                carta = {
                    "naipe": naipe,
                    "numero": str(numero),
                    "jogador": None
                }
                self.cartas.append(carta)
            for numero in ["Dama", "Valete", "Rei"]:
                carta = {
                    "naipe": naipe,
                    "numero": numero,
                    "jogador": None
                }
                self.cartas.append(carta)
        self.embaralha()
        self.__index_generator__ = 0

    def dar_as_cartas(self, jogador=Player()):
        for i in range(2):
            carta = self.cartas[self.__index_generator__]
            carta['jogador'] = jogador.name
            jogador.cards.append(carta)
            self.__index_generator__ += 1
        return jogador.cards

    def pedir_carta(self, jogador=Player()):
        carta = self.cartas[self.__index_generator__]
        carta['jogador'] = jogador.name
        jogador.cards.append(carta)
        self.__index_generator__ += 1
        return carta

    def embaralha(self):
        return random.shuffle(self.cartas)

    def somar_pontos(self, cartas):
        soma = 0
        for carta in cartas:
            if isinstance(carta['numero'], str):
                soma += 10
            else:
                if carta['numero'] == 1:
                    soma += 11
                    if soma > 21:
                        soma -= 10
                else:
                    soma += carta['numero']
        return soma
