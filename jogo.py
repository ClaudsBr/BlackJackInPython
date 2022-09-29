import itertools
import random
from time import sleep
import emoji

from faker import Faker
from baralho import Baralho
from negociante import Negociante
from jogador import Jogador
from jogador_ia import JogadorIA

jogar = True
class Jogo:

    def __init__(self):
        self.jogadores = []
        self.baralho = Baralho()
        self.ganhadores = []
        self.perdedores = []
        self.empatados = []
        self.aposta = {}

    def apostar(self, jogador: Jogador):
        self.aposta[jogador.id] = jogador.apostando()

    def definir_vencedor(self):
        partida = []
        negociante = self.jogadores.pop()

        for jogador in self.jogadores:
            vencedor = {}
            vencedor["jogador"] = jogador
            vencedor["pontuacao"] = jogador.pontuacao
            partida.append(vencedor)

        for jogador in partida:
            if (jogador['pontuacao'] <= 21):
                if(jogador['pontuacao'] > negociante.pontuacao):
                    jogador['jogador'].jogador_ganha(jogador['jogador'].aposta)
                    negociante.saldo -= jogador['jogador'].aposta
                    self.ganhadores.append(jogador['jogador'])
                elif(negociante.valores > 21):
                    jogador['jogador'].jogador_ganha(jogador['jogador'].aposta)
                    self.ganhadores.append(jogador['jogador'])
                elif(jogador['pontuacao'] == negociante.pontuacao):
                    jogador['jogador'].saldo += jogador['jogador'].aposta
                    self.empatados.append(jogador['jogador'])
                else:
                    self.perdedores.append(jogador['jogador'])

        self.mostrar_ganhadores()
        self.mostrar_perdedores()
        self.mostrar_empatados()
        self.saldo()

    def mostrar_ganhadores(self):
        print("Ganhador(es) da rodada:")
        for ganhador in self.ganhadores:
            print(ganhador.nome)
        print()

    def mostrar_perdedores(self):
        print("Perdedor(es) da Rodada:")
        for perdedor in self.perdedores:
            if perdedor.nome == "Dealer":
                break
            print(perdedor.nome)
        print()

    def mostrar_empatados(self):
        if len(self.empatados) == 0:
            print("Ninguém empatou com o Dealer")
        else:
            print('Empataram com o Dealer:')
            for jogador in self.empatados:
                print(jogador.nome)
        print()


    def saldo(self):
        print("Saldo dos participantes")
        for jogador in self.jogadores:
            print(jogador.nome, jogador.saldo)

    def pedir_carta(self, jogador: Jogador):
        self.baralho.pedir_carta(jogador)
        jogador.valores = self.baralho.somar_pontos(jogador.cartas)

    @staticmethod
    def definir_jogadores(jogadores_reais, numero_jogadores_artificiais):
        # Define o numero de participantes do jogo alem do dealer
        jogadores = []
        for nome in jogadores_reais:
            jogadores.append(Jogador(nome))

        for i in range(numero_jogadores_artificiais):
            jogador_artificial = JogadorIA()
            jogadores.append(jogador_artificial)

        negociante = Negociante()
        jogadores.append(negociante)
        return jogadores

    def definir_as_cartas_do_jogo(self):

        for jogador in self.jogadores:
            self.baralho.dar_as_cartas(jogador)

    def pedir_ou_manter(self, jogador: Jogador):
        # Pergunta se o jogador vai permanecer com as mesmas cartas ou pedir um outra carta
        while True:
            pergunta = jogador.jogando()

            if pergunta == 'p':

                self.pedir_carta(jogador)
                sleep(0.5)
                self.mostrar_cartas_do_jogador(jogador)
                if jogador.pontuacao > 21:
                    self.perdedores.append(jogador)
                    print(f"{jogador.nome} ESTOUROU e PERDEU {self.aposta[jogador.id]}!\nPontuação: {jogador.pontuacao} pontos\n"
                          f"Saldo Atual: {jogador.saldo}")
                    break

            elif pergunta == 'm':
                sleep(0.5)
                print(f"O jogador {jogador.nome} optou por permanecer com essas cartas")
                sleep(1)
                break
            else:
                sleep(0.5)
                print("Comando inválido, tente novamente")
                continue

    def mostrar_todas_as_cartas(self):
        sleep(1)
        print("--- RESULTADO FINAL ----")
        for jogador in self.jogadores:
            print("Jogador:", jogador.nome)
            print("Cartas:")
            print("---------------")
            for carta in jogador.cartas:
                print(f"{carta['numero']} {carta['naipe']}")
                sleep(0.3)
            print("---------------")
            print(f'Pontuação: {jogador.pontuacao}')
            sleep(0.5)
            print()

    def mostrar_cartas_do_jogador(self, jogador: Jogador):
        print("Jogador:", jogador.nome)
        print("Cartas:")
        print('-------------------')
        for carta in jogador.cartas:
            print(f"{carta['numero']} {carta['naipe']}")
            sleep(0.5)
        print('-------------------')
        self.calcular_pontuacao(jogador)
        print(f'Pontuação: {jogador.pontuacao}')
        sleep(0.3)

    def calcular_pontuacao(self, jogador: Jogador):
        jogador.pontuacao = self.baralho.somar_pontos(jogador.cartas)

    def nova_rodada(self):
        while True:
            pergunta = input("Deseja continuar? S/N")
            if pergunta[0].lower() == 's':
                for jogador in self.jogadores:
                    jogador.cards.clear()
                    self.ganhadores.clear()
                    self.perdedores.clear()
                self.baralho.embaralha()
                self.baralho.__index_generator = 0
                self.definir_as_cartas_do_jogo()
                for jogador in self.jogadores:
                    self.apostar()
                    self.mostrar_cartas_do_jogador()
                    self.calcular_pontuacao()
                    self.hit_ou_stand(jogador)
                self.mostrar_todas_as_cartas()
                self.vencedor()

            elif pergunta[0].lower() == 'n':
                print("FIM DO JOGO")
                self.saldo()
                break
            else:
                print("resposta incorreta, digite S para continuar ou N para sair do jogo")
                continue

    def jogar(self):

        self.introducao()
        self.definir_as_cartas_do_jogo()
        for jogador in self.jogadores:
            self.apostar(jogador)
            self.mostrar_cartas_do_jogador(jogador)
            self.calcular_pontuacao(jogador)
            self.pedir_ou_manter(jogador)
        self.mostrar_todas_as_cartas()
        self.definir_vencedor()
        '''self.nova_rodada()'''

    def introducao(self):
        print(emoji.emojize(":club_suit::heart_suit:Bem-vindo ao BlackJack!  :spade_suit::diamond_suit:"))

        while True:
            jogadores_reais = int(input("Digite a quantidade de pessoas da partida (Máximo 8 jogadores)\n"))
            if jogadores_reais <= 8:
                lista_jogadores = [input("Digite seu nome:\n") for i in range(jogadores_reais)]
                break
            else:
                print("Quantidade de Jogadores Inválida! O limite é de 8 jogadores\nTente Novamente!")
                continue

        while True:
            numero_jogadores_artificiais = int(input("Digite a quantidade de jogadores artificiais da partida\n"))
            if numero_jogadores_artificiais + jogadores_reais <= 8:
                self.jogadores = self.definir_jogadores(lista_jogadores, numero_jogadores_artificiais)
                break
            else:
                print(f"Quantidade Inválida! O limite é de 8 jogadores e já temos {jogadores_reais}")
                continue


if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
