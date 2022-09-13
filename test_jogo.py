import unittest
from unittest.mock import patch, MagicMock

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
        self.baralho.pedir_carta(self.jogador)
        esperado = 1
        resultado = len(self.jogador.cards)
        self.assertEqual(resultado, esperado)

    def test_definir_as_cartas_do_jogo(self):
        cartas = self.baralho.dar_as_cartas(self.jogador)
        esperado = 2
        resultado = len(cartas)
        self.assertEqual(resultado, esperado)
        print(self.jogador.cards)

    def test_numero_de_jogadores_igual_a_3(self):
        numero_de_jogadores = 3
        esperado = numero_de_jogadores + 1 # numero de jogadores + dealer
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


    @patch("jogo.Jogo.mostrar_as_cartas")
    def test_mostrar_as_cartas(self, mostrar_as_cartas_mock: MagicMock):
        jogador = Player()
        dealer = Dealer()
        baralho = Baralho()
        baralho.dar_as_cartas(dealer)
        baralho.dar_as_cartas(jogador)
        jogadores = [dealer, jogador]
        jogo = Jogo()
        jogo.jogadores = jogadores
        mostrar_as_cartas_mock.side_effect = "Jogador: Dealer" \
                                             "Cartas:" \
                                             "{'naipe': 'Paus', 'numero': '8', 'jogador': 'Dealer', " \
                                             "'id': '0bb64b4b-299c-444c-9ee5-a1f82d9f782f'}" \
                                             "{'naipe': 'Copas', 'numero': '3', 'jogador': 'Dealer', " \
                                             "'id': 'a343e54f-3f18-44d3-b1b7-ed9bf25f9b40'}" \
                                             "Jogador: Maria Morgan" \
                                             "Cartas:" \
                                             "{'naipe': 'Ouros', 'numero': 'Valete', 'jogador': 'Maria Morgan', " \
                                             "'id': '68ddec54-af10-40e7-8b51-306d20cd79ef'}" \
                                             "{'naipe': 'Copas', 'numero': 'Valete', 'jogador': 'Maria Morgan', " \
                                             "'id': '402b6e8c-7b63-4c2c-9c79-75e628b6b04b'}"
        resposta = self.jogo.mostrar_as_cartas()
        print(resposta)







