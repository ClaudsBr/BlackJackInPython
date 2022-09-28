import random
from jogador import Jogador
from uuid import uuid4
import emoji

class Baralho():

    def __init__(self):

        self.cartas = []
        paus = emoji.emojize(":club_suit:")
        copas = emoji.emojize(":heart_suit:")
        espadas = emoji.emojize(":spade_suit:")
        ouros = emoji.emojize(":diamond_suit:")
        for naipe in [paus, copas, espadas, ouros]:
            for numero in range(2, 11):
                carta = {
                    "naipe": naipe,
                    "numero": str(numero),
                    "jogador": None,
                    "id": str(uuid4())
                }
                self.cartas.append(carta)

            for numero in ["A", "Q", "J", "K"]:
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
            if (carta["numero"] == "K") \
                    or (carta["numero"] == "Q") \
                    or (carta["numero"] == "J"):
                soma += 10
                valores.append(carta['numero'])
            elif(carta["numero"]== "A"):
                soma +=1
                valores.append(carta['numero'])
            else:
                soma += int(carta['numero'])
                valores.append(int(carta['numero']))

        if "A" in valores:
            if ("K" in valores) \
                    or ("Q" in valores) \
                    or ("J" in valores):
                soma += 10
                if soma > 21:
                    soma -= 10
        return soma

    def exibir_cartas(self):
        for carta in self.cartas:
            print(f"{carta['numero']} {carta['naipe']}")


