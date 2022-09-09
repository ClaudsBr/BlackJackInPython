from faker import Faker
from baralho import Baralho
from dealer import Dealer
from player import Player

jogar = True
class Jogo:

    def __init__(self):
        self.jogadores = []
        self.baralho = Baralho()

    def apostar(self, jogador : Player):
        aposta = int(input("Digite o valor da sua aposta:\n"))
        if jogador.values == self.vencedor():
            jogador.balance += aposta
            self.mostrar_as_cartas()
            print(f"Parabens!\nVocê Ganhou {aposta} nesta rodada!\n"
                  f"Seu saldo atual é de {jogador.balance}")
        else:
            jogador.balance -= aposta
            self.mostrar_as_cartas()
            print(f"Você Perdeu {aposta} nesta rodada!\n"
                  f"Seu saldo atual é de {jogador.balance}")

    def vencedor(self):
        partida = []
        pontos = 0
        for jogador in self.jogadores:
            rodada = {}
            rodada["nome"] = jogador.name
            rodada["pontuacao"] = jogador.values
            partida.append(rodada)

        for item in partida:
            if (item['pontuacao'] <= 21 ) and (item['pontuacao'] > pontos):
                pontos = item['pontuacao']

        return pontos


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
        global jogar

        while True:
            pergunta = input("Digite H para dar HIT ou S para STAND\n")

            if pergunta[0].lower() == 'h':
                self.pedir_carta(self.jogadores[1])
                jogar = True
            elif pergunta[0].lower() == 's':
                print("Você optou por permanecer com as mesmas cartas")
                jogar = False
            else:
                print("Comando inválido, tente novamente")
                continue
            break


    def mostrar_as_cartas(self):
        for jogador in self.jogadores:
            print("Jogador:", jogador.name)
            print("Cartas:")
            for carta in jogador.cards:
                print(carta)
            print()

    def calcular_pontuacao(self):
        for jogador in self.jogadores:
            jogador.values = self.baralho.somar_pontos(jogador.cards)




