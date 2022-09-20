import itertools
import random

from faker import Faker
from baralho import Baralho
from dealer import Dealer
from player import Player


jogar = True
class Jogo:

    def __init__(self):
        self.jogadores = []
        self.baralho = Baralho()
        self.ganhadores = []
        self.perdedores = []

    def apostar(self):
        while True:
            try:
                self.aposta = int(input("Digite o valor da sua aposta\n"))
            except ValueError:
                print("Valor não aceito")
            else:
                if self.jogadores[1].balance < self.aposta:
                    print("Saldo Insuficiente")
                else:
                    break

    '''def apostar(self):
        apostas = itertools.cycle(self.jogadores)
        for aposta in apostas:
            self.aposta = aposta
        print(f"O valor de aposta da rodada é: {self.aposta}")'''

    def vencedor(self):
        partida = []
        maior_pontuacao = 0

        for jogador in self.jogadores:
            vencedor = {}
            vencedor["jogador"] = jogador
            vencedor["pontuacao"] = jogador.values
            partida.append(vencedor)

        for jogador in partida:
            if (jogador['pontuacao'] < 22):
                if(jogador['pontuacao'] >= maior_pontuacao):
                    maior_pontuacao = jogador['pontuacao']

        for jogador in partida:
            if jogador['pontuacao'] == maior_pontuacao:
                self.ganhadores.append(jogador)


        print("Ganhador da rodada:")
        for ganhador in self.ganhadores:
            ganhador['jogador'].balance += self.aposta
            print(ganhador['jogador'].name)


        for jogador in partida:
            if jogador['pontuacao'] != maior_pontuacao:
                self.perdedores.append(jogador)

        for perdedor in self.perdedores:
            perdedor['jogador'].balance -= self.aposta

        self.saldo()

    def saldo(self):
        for jogador in self.jogadores:
            print("Saldodos participantes")
            print(jogador.name, jogador.balance)

    def pedir_carta(self, jogador: Player):
        self.baralho.pedir_carta(jogador)
        jogador.values = self.baralho.somar_pontos(jogador.cards)

    def definir_jogadores(self):
        # Define o numero de participantes do jogo alem do dealer
        numero_jogadores = int(input("Digite a quantidade de jogadores da partida\n"))
        nome = input("Digite seu nome:\n")
        jogador = Player(nome)
        dealer = Dealer()
        self.jogadores = [dealer, jogador]
        for i in range(numero_jogadores-1):
            jogador = Player(name=Faker().name())
            self.jogadores.append(jogador)

    def definir_as_cartas_do_jogo(self):
        for jogador in self.jogadores:
            self.baralho.dar_as_cartas(jogador)

    def hit_ou_stand(self):
        # Pergunta se o jogador vai permanecer com as mesmas cartas ou pedir um outra carta

        while True:

            pergunta = input("Digite H para dar HIT ou S para STAND\n")

            if pergunta[0].lower() == 'h':
                self.pedir_carta(self.jogadores[1])
                if self.jogadores[1].values > 21:
                    print(f"VOCÊ PERDEU {self.aposta}!\nSua Pontuação: {self.jogadores[1].values} pontos\nSeu saldo Atual é {self.jogadores[1].balance}")
                    break
                self.mostrar_cartas_do_jogador()
            elif pergunta[0].lower() == 's':
                print("Você optou por permanecer com as mesmas cartas")
                break
            else:
                print("Comando inválido, tente novamente")
                continue


    def mostrar_todas_as_cartas(self):
        for jogador in self.jogadores:
            print("Jogador:", jogador.name)
            print("Cartas:")
            for carta in jogador.cards:
                print(carta)
            print(f'Pontuação: {jogador.values}')
            print()

    def mostrar_cartas_do_jogador(self):
        print("Jogador:", self.jogadores[1].name)
        print("Cartas:")
        for carta in self.jogadores[1].cards:
            print(carta)

    def calcular_pontuacao(self):
        for jogador in self.jogadores:
            jogador.values = self.baralho.somar_pontos(jogador.cards)
            if self.jogadores[0].values < 17:
                self.pedir_carta(self.jogadores[0])

            '''if self.jogadores[0].values > 21:
                self.jogadores[0].dealer_lose(self.aposta)'''

        for jogador in self.jogadores[2:]:
            valores = [15,16,17,18]
            escolha = random.choice(valores)
            if jogador.values < escolha:
                self.pedir_carta(jogador)
                if jogador.values < escolha:
                    self.pedir_carta(jogador)

            '''if jogador.values > 21:
                jogador.player_lose(self.aposta)'''


    def jogador_perde(self):
        self.jogadores[1].player_lose(self.aposta)
        print(f"Você perdeu {self.aposta}\nSeu saldo atual é {self.jogadores[1].balance}")

    def jogador_ganha(self):
        self.jogadores[1].player_win(self.aposta)
        print(f"Parabéns!\nVocê ganhou {self.aposta}\nSeu saldo atual é {self.jogadores[1].balance}")
    def jogar(self):
        print("Bem vindo ao BlackJack!")
        self.definir_jogadores()
        self.definir_as_cartas_do_jogo()
        self.apostar()
        self.mostrar_cartas_do_jogador()
        self.calcular_pontuacao()
        self.hit_ou_stand()
        self.mostrar_todas_as_cartas()
        self.vencedor()


jogo = Jogo()
jogo.jogar()
