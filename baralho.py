import random
from player import Player
from uuid import uuid4


class Baralho():

    def __init__(self):

        self.cartas = []
        for naipe in ["Paus", "Copas", "Espadas", "Ouros"]:
            for numero in range(1, 11):
                carta = {
                    "naipe": naipe,
                    "numero": str(numero),
                    "jogador": None,
                    "id": str(uuid4())
                }
                self.cartas.append(carta)

            for numero in ["Dama", "Valete", "Rei"]:
                carta = {
                    "naipe": naipe,
                    "numero": numero,
                    "jogador": None,
                    "id": str(uuid4())
                }
                self.cartas.append(carta)
        self.embaralha()
        self.__index_generator = 0

    def dar_as_cartas(self, jogador: Player):

        return [self.pedir_carta(jogador), self.pedir_carta(jogador)]

    def pedir_carta(self, jogador: Player):
        carta = self.cartas[self.__index_generator]
        carta['jogador'] = jogador.name
        jogador.cards.append(carta)
        self.__index_generator += 1
        return carta

    def embaralha(self):
        return random.shuffle(self.cartas)

    def somar_pontos(self, cartas):
        soma = 0
        valores = []
        for carta in cartas:
            if (carta["numero"] == "Rei") \
                    or (carta["numero"] == "Dama") \
                    or (carta["numero"] == "Valete"):
                soma += 10
                valores.append(carta["numero"])
            else:
                soma += int(carta['numero'])
                valores.append(int(carta['numero']))

        if 1 in valores:
            if ("Rei" in valores) \
                    or ("Dama" in valores) \
                    or ("Valete" in valores):
                soma += 10
                if soma > 21:
                    soma -= 10

        return soma


