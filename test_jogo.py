import unittest
from unittest.mock import patch, MagicMock

from baralho import Baralho
from jogador_ia import JogadorIA
from negociante import Negociante
from jogo import Jogo
from jogador import Jogador


class TestJogo(unittest.TestCase):

    def setUp(self):
        self.jogo = Jogo()
        self.baralho = Baralho()
        self.jogador = Jogador()
        self.jogador_ia = JogadorIA()

    def test_pedindo_carta(self):
        self.baralho.pedir_carta(self.jogador)
        esperado = 1
        resultado = len(self.jogador.cartas)
        self.assertEqual(resultado, esperado)

    def test_definir_as_cartas_do_jogo(self):
        cartas = self.baralho.dar_as_cartas(self.jogador)
        esperado = 2
        resultado = len(cartas)
        self.assertEqual(resultado, esperado)
        print(self.jogador.cartas)

    def test_numero_de_jogadores_reais_igual_a_1_e_jogadores_artificiais_igual_1(self):
        esperado = 3 # 1 jogador real + 1 jogador artificial + dealer
        jogadores = self.jogo.definir_jogadores(['nome_do_jogador'], 1)
        resultado = len(jogadores)

        self.assertEqual(esperado, resultado)


    def test_calculo_dos_pontos(self):
        cartas_jogador = [
            {"naipe": ":diamond_suit:", "numero": "8", "jogador": None,
             "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": ":heart_suit:", "numero": "10", "jogador": None,
             "id": "e4d9c608-6019-4ef5-9258-4dc8276f6cc8"}
        ]
        esperado = 18
        self.jogador.cartas = cartas_jogador
        self.jogador.pontuacao = self.baralho.somar_pontos(self.jogador.cartas)
        resultado = self.jogador.pontuacao
        self.assertEqual(resultado, esperado)






