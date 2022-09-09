import unittest

from baralho import Baralho
from dealer import Dealer
from jogo import Jogo
from player import Player


class TestJogo(unittest.TestCase):

    def setUp(self):
        self.jogo = Jogo()
        self.baralho = Baralho()
        self.jogador = Player()

    def test_pedindo_carta(self):
        carta = self.baralho.pedir_carta(self.jogador)
        esperado = 1
        resultado = len(self.jogador.cards)
        self.assertEqual(resultado, esperado)

    def test_definir_as_cartas_do_jogo(self):
        cartas = self.baralho.dar_as_cartas(self.jogador)
        esperado = 2
        resultado = len(cartas)
        self.assertEqual(resultado, esperado)
        print(self.jogador.cards)

    def test_definir_numero_de_jogadores(self):
        jogador = Player("Clemente Raul")
        dealer = Dealer()
        jogadores = [dealer, jogador]
        esperado = len(jogadores)
        self.jogo.definir_jogadores()
        resultado = len(self.jogo.jogadores)
        self.assertEqual(esperado, resultado)

    def test_calculo_dos_pontos(self):
        cartas_jogador = [
            {"naipe": "Ouros", "numero": "8", "jogador": None,
             "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": "Copas", "numero": "10", "jogador": None,
             "id": "e4d9c608-6019-4ef5-9258-4dc8276f6cc8"}
        ]
        esperado = 18
        self.jogador.cards = cartas_jogador
        self.jogador.values = self.baralho.somar_pontos(self.jogador.cards)
        resultado = self.jogador.values
        self.assertEqual(resultado, esperado)






