import time
from baralho import Baralho
from player import Player
import random
'''
random.seed()

baralho = Baralho()

print(len(baralho.cartas)) # Tamanho do Dicionario
print(baralho.cartas) # Lista na Ordem Original
random.shuffle(baralho.cartas) # embaralhando as cartas

user = []
dealer = []
user.append(baralho.cartas.pop())
user.append(baralho.cartas.pop())
print(user)
dealer.append(baralho.cartas.pop())
dealer.append(baralho.cartas.pop())
print(dealer)
#usuario.append(baralho.cartas.pop())

#print(f'tirando a carta: {baralho.cartas.pop(carta_aleatoria)}')

print(f'tamanho do baralho = {len(baralho.cartas)}')

print(baralho.cartas)


#print(f'tirando a carta: {baralho.cartas.pop(carta_aleatoria)}')
#print(f'tamanho do baralho = {len(baralho.cartas)}')

print(baralho.cartas)

novo_baralho = Baralho()
print(novo_baralho.cartas)
novo_baralho.embaralha()
print(novo_baralho.cartas)

novo_baralho.embaralha()
print(novo_baralho.cartas)
novo_baralho.dar_as_cartas()
print(novo_baralho.dealer)
print(novo_baralho.player)
novo_baralho.pedir_carta()
print(novo_baralho.player)
novo_baralho.pedir_carta()
print(novo_baralho.player)

from faker import Faker

fake = Faker()

print(fake.name())

from player import Player

player1 = Player()
print(player1.name)
player2 = Player("João")
print(player2.name)

from itertools import repeat, cycle

x = repeat(list(range(1,6)),10)
print(x)

for i in x:
    print(i)

y = cycle(list(range(1,11)))
while True:
    print(next(y))
    time.sleep(1)

novo_baralho = Baralho()
# Baralho não é um objeto iteravel, porem o atributo cartas é iteravel
lista_de_nomes_aleatorios = []
nome_fake = Faker()
for i in range(0,20):
    lista_de_nomes_aleatorios.append(nome_fake.name())

z = cycle(novo_baralho.cartas)
print(next(z))

i = 1
while True:
    print(i, next(z))
    time.sleep(1)
    i +=1

baralho = Baralho()
jogador = Player()
jogo = cycle(baralho.cartas)

print(baralho.cartas)
baralho.embaralha()
baralho.embaralha()
print(baralho.cartas)

for i in range(2):
    jogador.cards.append(next(jogo))
    baralho.cartas[i]['jogador'] = jogador.name
print('........................')
print(jogador.cards)
print(baralho.cartas)
jogador2 = Player()
baralho2 = Baralho()
print("=====================")
print(jogador2.jogar())
print(baralho2.cartas)
print('---------------------')
jogador3 = Player("Teobaldo")
baralho.embaralha()
print(jogador3.name)

import random


class BaralhoGenerator:
    def __init__(self):
        self.cartas = [1, 2, 3, 4, 5]
        random.shuffle(self.cartas)
        self.__index_generator__ = self.__get_index__()

    def __get_index__(self):
        for i in range(self.cartas.__len__()):
            yield i

    def get_carta(self):
        return self.cartas[next(self.__index_generator__)]


class BaralhoIndex:
    def __init__(self):
        self.cartas = [1, 2, 3, 4, 5]
        random.shuffle(self.cartas)
        self.__index_generator__ = 0

    def get_carta(self):
        carta = self.cartas[self.__index_generator__]
        self.__index_generator__ += 1

        return carta

baralho = BaralhoGenerator()
carta = baralho.get_carta()

print(carta)

baralho2 = BaralhoIndex()
carta2 = baralho2.get_carta()
print(carta2)
from player import Player
'''
baralho = Baralho()
jogador1 = Player()
jogador2 = Player("Rivaldo")

print("Testando os nomes dos jogadores ",jogador1.name, " e ", jogador2.name)
print(f'Cartas {jogador1.name}\n{baralho.dar_as_cartas(jogador1)}\nCartas {jogador2.name}\n{baralho.dar_cartas(jogador2)}')
print()
print(baralho.cartas)
print(f"Jogador {jogador2.name} pedindo uma carta")
print(baralho.pedir_carta(jogador2))
print(f'Cartas {jogador2.name}\n{jogador2.cards}')