import unittest
from unittest.mock import patch
from io import StringIO
from jogador import Jogador
from jogo import Jogo


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.jogador = Jogador()
        self.jogo = Jogo()

    @patch('sys.stdin', StringIO('300\n'))
    def test_metodo_jogador_ganha_o_valor_300(self):
        aposta = 300
        esperado = 3300
        self.jogador.apostando()
        self.jogador.jogador_ganha(aposta)
        resultado = self.jogador.saldo
        self.assertEqual(resultado, esperado)

    @patch('sys.stdin', StringIO('300\n'))
    def test_jogador_aposta_o_valor_300(self):
        aposta = 300
        esperado = 2700
        self.jogador.apostando()
        resultado = self.jogador.saldo
        self.assertEqual(resultado, esperado)

    @patch('sys.stdin', StringIO('H\n'))
    def test_jogada_h(self):
        esperado = 'h'
        jogada =self.jogador.jogando()
        self.assertEqual(jogada, esperado)
