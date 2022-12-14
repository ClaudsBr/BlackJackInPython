from time import sleep
import emoji

from baralho import Baralho
from constantes import VERMELHO, AZUL, VERDE, AMARELO, BRANCO
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
        self.jogadores[-1].saldo += jogador.aposta

    def vencedor(self, jogador: Jogador):
        negociante = self.jogadores[-1]
        if ((jogador.pontuacao <= 21) and (negociante.pontuacao > 21)) or \
                ((jogador.pontuacao <= 21) and
                 (jogador.pontuacao > negociante.pontuacao)):
            jogador.jogador_ganha(jogador.aposta)
            negociante.negociante_perde(jogador)
            self.ganhadores.append(jogador)
        elif jogador.pontuacao <= 21 and \
                jogador.pontuacao == negociante.pontuacao:
            jogador.jogador_empata(jogador.aposta)
            self.empatados.append(jogador)
        elif jogador.pontuacao < 21 and \
                jogador.pontuacao < negociante.pontuacao:
            self.perdedores.append(jogador)

    def definir_vencedor_da_rodada(self):
        for jogador in self.jogadores:
            self.vencedor(jogador)
        self.mostrar_ganhadores()
        self.mostrar_perdedores()
        self.mostrar_empatados()

    def mostrar_ganhadores(self):
        print("Ganhador(es) da rodada:")
        for ganhador in self.ganhadores:
            if ganhador.nome != "Dealer":
                print(ganhador.nome)
        print()

    def mostrar_perdedores(self):
        print("Perdedor(es) da Rodada:")
        for perdedor in self.perdedores:
            if perdedor.nome == "Dealer":
                break
            print(perdedor.nome)
        else:
            print()

    def mostrar_empatados(self):
        print()
        if len(self.empatados) == 0:
            print("Ningu??m empatou com o Dealer")
        else:
            print('Empataram com o Dealer:')
            for jogador in self.empatados:
                if jogador.nome != "Dealer":
                    print(jogador.nome)
        print()

    def pedir_carta(self, jogador: Jogador):
        self.baralho.pedir_carta(jogador)
        jogador.valores = self.baralho.somar_pontos(jogador.cartas)

    @staticmethod
    def definir_jogadores(jogadores_reais, numero_jogadores_artificiais):
        # Define o numero de participantes do jogo alem do dealer
        jogadores = []
        for i, nome in enumerate(jogadores_reais):
            jogadores.append(Jogador(nome))
            print(f'{AZUL}Jogador real de nome {jogadores[i].nome} '
                  f'e id: {jogadores[i].id[:5]} criado com sucesso!{BRANCO}')

        for i in range(numero_jogadores_artificiais):
            jogador_artificial = JogadorIA()
            print(f'{AZUL}Jogador artificial de nome '
                  f'{jogador_artificial.nome} '
                  f'e id: {jogador_artificial.id[:5]} '
                  f'criado com sucesso!{BRANCO}')
            jogadores.append(jogador_artificial)

        negociante = Negociante()
        jogadores.append(negociante)
        return jogadores

    def definir_as_cartas_do_jogo(self):

        for jogador in self.jogadores:
            self.baralho.dar_as_cartas(jogador)

    def pedir_ou_manter(self, jogador: Jogador):
        # Pergunta se o jogador vai pedir uma nova carta P
        # ou se vai manter as mesmas cartas M
        while True:
            pergunta = jogador.jogando()

            if pergunta == 'p':

                self.pedir_carta(jogador)
                sleep(0.5)
                self.mostrar_cartas_do_jogador(jogador)
                if jogador.pontuacao > 21:
                    self.perdedores.append(jogador)
                    print(f"{VERMELHO}{jogador.nome} ESTOUROU e "
                          f"PERDEU {BRANCO}"
                          f"{self.aposta[jogador.id]}!"
                          f"\nPontua????o: {jogador.pontuacao} pontos"
                          )
                    break

            elif pergunta == 'm':
                sleep(0.5)
                print(f"O jogador {jogador.nome} optou por "
                      f"permanecer com essas cartas")
                sleep(1)
                break
            else:
                sleep(0.5)
                print("Comando inv??lido, tente novamente")
                continue

    def mostrar_todas_as_cartas(self):
        sleep(1)
        print(f"{AMARELO}--- RESULTADO FINAL ----{BRANCO}")
        sleep(0.5)
        for jogador in self.jogadores:
            print("Jogador:", jogador.nome)
            print("Cartas:")
            print("---------------")
            for carta in jogador.cartas:
                print(f"{carta['numero']} {carta['naipe']}")
            print("---------------")
            print(f'Pontua????o: {jogador.pontuacao}')
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
        print(f'Pontua????o: {jogador.pontuacao}')
        sleep(0.3)

    def calcular_pontuacao(self, jogador: Jogador):
        jogador.pontuacao = self.baralho.somar_pontos(jogador.cartas)

    def devolver_as_cartas(self):
        for jogador in self.jogadores:
            jogador.cartas.clear()

    def iniciar_nova_rodada(self):
        self.devolver_as_cartas()
        self.baralho = Baralho()
        self.baralho.embaralha()
        self.ganhadores.clear()
        self.perdedores.clear()
        self.empatados.clear()

    def continuar(self):
        for jogador in self.jogadores:
            pergunta = jogador.continuando()
            if pergunta.lower() == 's':
                print(f'{AZUL}O jogador {jogador.nome} '
                      f'vai continuar no jogo{BRANCO}')
            else:
                jogador.desativar()
                self.jogadores.remove(jogador)
                self.sair_do_jogo(jogador)

    def jogadores_reais_ativos(self):
        if type(self.jogadores[0]) == Jogador:
            self.nova_rodada()
        else:
            self.fim_de_jogo()

    def fim_de_jogo(self):
        print(f'\n{VERMELHO}========= FIM DE JOGO =========')
        print(f"{VERDE}Obrigado por Jogar o BlackJack!!!")

    def nova_rodada(self):

        while True:

            self.iniciar_nova_rodada()
            self.definir_as_cartas_do_jogo()

            for jogador in self.jogadores:

                self.apostar(jogador)
                self.mostrar_cartas_do_jogador(jogador)
                self.calcular_pontuacao(jogador)
                self.pedir_ou_manter(jogador)
            self.mostrar_todas_as_cartas()
            self.definir_vencedor_da_rodada()
            self.continuar()
            self.jogadores_reais_ativos()
            break

    def sair_do_jogo(self, jogador: Jogador):

        print(
            f"{VERMELHO}O jogador {jogador.nome} saiu do jogo{BRANCO}\n"
              )

    def jogar(self):

        self.introducao()
        self.definir_as_cartas_do_jogo()
        for jogador in self.jogadores:
            self.apostar(jogador)
            self.mostrar_cartas_do_jogador(jogador)
            self.calcular_pontuacao(jogador)
            self.pedir_ou_manter(jogador)
        self.mostrar_todas_as_cartas()
        self.definir_vencedor_da_rodada()
        self.continuar()
        self.jogadores_reais_ativos()

    def introducao(self):
        print(emoji.emojize(":club_suit::heart_suit:"
                            f"{AMARELO}Bem-vindo ao BlackJack!{BRANCO}  "
                            ":spade_suit::diamond_suit:"))

        while True:
            jogadores_reais = int(input("Digite a quantidade "
                                        "de jogadores reais da partida "
                                        "(M??ximo de 8 jogadores)\n"))
            if jogadores_reais <= 8:
                lista_jogadores = []
                for indice in range(jogadores_reais):
                    nome = input(f'Digite o nome do {indice + 1}?? jogador\n')
                    lista_jogadores.append(nome)
                break
            else:
                print("Quantidade de Jogadores Inv??lida! "
                      "O limite ?? de 8 jogadores\nTente Novamente!")
                continue

        while True:
            numero_jogadores_artificiais = int(input(
                "Digite a quantidade de jogadores artificiais da partida\n"))
            if numero_jogadores_artificiais + jogadores_reais <= 8:
                self.jogadores = self.definir_jogadores(
                    lista_jogadores, numero_jogadores_artificiais
                )
                break
            else:
                print(f"Quantidade Inv??lida! "
                      f"O limite de jogadores articiais pra essa partida ?? "
                      f"de {8 - jogadores_reais} jogadores e "
                      f"j?? temos {jogadores_reais} jogador real")
                continue


if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
