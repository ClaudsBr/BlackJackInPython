import unittest

from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.jogador = Player()

    def test_quando_o_jogador_ganha_300(self):
        bet = 300
        esperado = 3300
        self.jogador.player_win(bet)
        resultado = self.jogador.balance
        self.assertEqual(resultado, esperado)

    def test_quando_o_jogador_perde_300(self):
        bet = 300
        esperado = 2700
        self.jogador.player_lose(bet)
        resultado = self.jogador.balance
        self.assertEqual(resultado, esperado)