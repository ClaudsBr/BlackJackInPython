from faker import Faker
from baralho import Baralho
from dealer import Dealer
from player import Player

jogar = True
class Jogo:

    def __init__(self):
        self.jogadores = []
        self.baralho = Baralho()

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

    def vencedor(self):
        partida = []
        maior_pontuacao = 0
        for jogador in self.jogadores:
            vencedor = {}
            vencedor["jogador"] = jogador
            vencedor["pontuacao"] = jogador.values
            partida.append(vencedor)

        for jogador in partida:
            if (jogador['pontuacao'] <= 21) and (jogador['pontuacao'] > maior_pontuacao):
                maior_pontuacao = jogador['pontuacao']

        if vencedor['jogador'] == self.jogadores[1]:
            self.jogador_ganha(self.aposta)
        else:
            self.jogador_perde(self.aposta)

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
        self.jogando = True
        while self.jogando:
            pergunta = input("Digite H para dar HIT ou S para STAND\n")

            if pergunta[0].lower() == 'h':
                self.pedir_carta(self.jogadores[1])
                self.mostrar_cartas_do_jogador()
            elif pergunta[0].lower() == 's':
                print("Você optou por permanecer com as mesmas cartas")
                self.jogando = False
            else:
                print("Comando inválido, tente novamente")
                continue
            break

    def mostrar_todas_as_cartas(self):
        for jogador in self.jogadores:
            print("Jogador:", jogador.name)
            print("Cartas:")
            for carta in jogador.cards:
                print(carta)
            print()

    def mostrar_cartas_do_jogador(self):
        print("Jogador:", self.jogadores[1].name)
        print("Cartas:")
        for carta in self.jogadores[1].cards:
            print(carta)

    def calcular_pontuacao(self):
        for jogador in self.jogadores:
            jogador.values = self.baralho.somar_pontos(jogador.cards)

    def jogador_perde(self, aposta):
        self.jogadores[1].player_lose(aposta)

    def jogador_ganha(self, aposta):
        self.jogadores[1].player_win(aposta)

    def jogar(self):
        print("Bem vindo ao BlackJack!")
        self.jogar = True
        self.definir_jogadores()
        self.definir_as_cartas_do_jogo()
        self.apostar()
        self.mostrar_cartas_do_jogador()
        self.hit_ou_stand()
        self.calcular_pontuacao()
        self.mostrar_todas_as_cartas()
        self.vencedor()

jogo = Jogo()
jogo.jogar()