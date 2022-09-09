import unittest

from dealer import Dealer


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()

    def test_quando_o_dealer_ganha_500(self):
        bet = 500
        esperado = 100500
        self.dealer.dealer_win(bet)
        resultado = self.dealer.balance
        self.assertEqual(resultado, esperado)

    def test_quando_o_dealer_perde_500(self):
        bet = 500
        esperado = 99500
        self.dealer.dealer_lose(bet)
        resultado = self.dealer.balance
        self.assertEqual(resultado, esperado)



