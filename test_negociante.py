import unittest
from unittest.mock import patch
from io import StringIO
from jogador import Jogador
from negociante import Negociante


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.negociante = Negociante()
        self.jogador = Jogador()

    @patch("sys.stdin", StringIO("500\n"))
    def test_quando_o_negociante_ganha_500(self):

        esperado = 100500
        self.jogador.apostando()

        resultado = self.negociante.saldo
        self.assertEqual(resultado, esperado)

    def test_quando_o_dealer_perde_500(self):
        bet = 500
        esperado = 99500
        self.dealer.dealer_lose(bet)
        resultado = self.dealer.balance
        self.assertEqual(resultado, esperado)



