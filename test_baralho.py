
from baralho import Baralho
from player import Player
import unittest
from unittest.mock import patch, MagicMock
import random


class TestBaralho(unittest.TestCase):

    def setUp(self):
        random.seed(10)
        self.baralho = Baralho()


    def test_somar_pontos_numeros(self):
        cartas = [
            {"naipe": "Ouros", "numero": "8", "jogador": None, "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": "Copas", "numero": "2", "jogador": None, "id": "e4d9c608-6019-4ef5-9258-4dc8276f6cc8"},
            {"naipe": "Espadas", "numero": "9", "jogador": None, "id": "5f036d20-9534-47e1-9d6d-4424cb9298d4"}
        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 19)


    def test_somar_pontos_figuras(self):
        cartas = [
            {"naipe": "Copas", "numero": "Rei", "jogador": None, "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},
            {"naipe": "Espadas", "numero": "Valete", "jogador": None, "id": "eeb5f5ad-083b-46a0-9b5f-ff63eec12940"}
        ]

        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 20)


    def test_somar_pontos_com_as(self):
        cartas = [
            {"naipe": "Ouros", "numero": "8", "jogador": None, "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": "Espadas", "numero": "1", "jogador": None, "id": "bebb9f09-19ae-46a0-8bab-0bcaa543f4c4"},
            {"naipe": "Copas", "numero": "Rei", "jogador": None, "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},
            {"naipe": "Ouros", "numero": "1", "jogador": None, "id": "32601ad5-a8c4-462e-811f-eed2914f105f"}
        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 20)


    def test_somar_pontos_21_valete(self):
        cartas = [

            {"naipe": "Ouros", "numero": "1", "jogador": None, "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": "Espadas", "numero": "Valete", "jogador": None, "id": "eeb5f5ad-083b-46a0-9b5f-ff63eec12940"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)


    def test_somar_pontos_21_rei(self):
        cartas = [

            {"naipe": "Ouros", "numero": "1", "jogador": None, "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": "Copas", "numero": "Rei", "jogador": None, "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)


    def test_somar_pontos_21_dama(self):
        cartas = [

            {"naipe": "Ouros", "numero": "1", "jogador": None, "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": "Copas", "numero": "Dama", "jogador": None, "id": "0b2a08d4-216a-412b-b02f-284493adf47d"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)


    def test_naipe_paus(self):
        achar_paus = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == "Paus":
                achar_paus = True

        self.assertTrue(achar_paus)


    def test_naipe_copas(self):
        achar_copas = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == "Copas":
                achar_copas = True

        self.assertTrue(achar_copas)


    def test_naipe_espadas(self):
        achar_espadas = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == "Espadas":
                achar_espadas = True

        self.assertTrue(achar_espadas)

    def test_naipe_ouros(self):
        achar_ouros = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == "Ouros":
                achar_ouros = True

        self.assertTrue(achar_ouros)

    def test_quantidade_cartas(self):
        tamanho = len(self.baralho.cartas)
        self.assertEqual(tamanho, 52)

    def test_valor_rei(self):
        achar_rei = False
        for carta in self.baralho.cartas:
            if carta["numero"] == "Rei":
                achar_rei = True

        self.assertTrue(achar_rei)

    def test_valor_dama(self):
        achar_dama = False
        for carta in self.baralho.cartas:
            if carta["numero"] == "Dama":
                achar_dama = True
        self.assertTrue(achar_dama)

    def test_valor_valete(self):
        achar_valete = False
        for carta in self.baralho.cartas:
            if carta['numero'] == "Valete":
                achar_valete = True
        self.assertTrue(achar_valete)

    def test_nome_jogador_na_carta(self):
        jogador = Player()
        cartas = self.baralho.dar_as_cartas(jogador)
        self.assertEqual(jogador.cards, cartas)


    def test_chave_jogador(self):
        achar_jogador = False
        jogador = Player()
        carta = self.baralho.pedir_carta(jogador)
        if carta['jogador'] == jogador.name:
            achar_jogador = True

        self.assertTrue(achar_jogador)

    def test_carta_com_jogador(self):
        chave = 'jogador'
        flag = False
        carta = self.baralho.cartas[0]
        for key in carta.items():
            if key[0] == chave:
                flag = True

        self.assertTrue(flag)





    @patch("baralho.Baralho.pedir_carta")
    def test_dar_as_cartas(self, pedir_carta_mock: MagicMock):
        jogador = Player()
        pedir_carta_mock.side_effect = [
            {"naipe": "Ouros", "numero": "Valete", "jogador": jogador.name},
            {"naipe": "Paus", "numero": "Valete", "jogador": jogador.name},
        ]
        resposta = self.baralho.dar_as_cartas(jogador)
        print(resposta)



    @patch("baralho.Baralho.pedir_carta", MagicMock(side_effect=[
            {"naipe": "Ouros", "numero": "Valete", "jogador": "Claudio"},
            {"naipe": "Paus", "numero": "Valete", "jogador": "Claudio"},
        ]))
    def test_dar_as_cartas2(self):
        jogador = Player("Claudio")
        resposta = self.baralho.dar_as_cartas(jogador)
        print(resposta)


    @patch("baralho.Baralho.pedir_carta")
    def test_dar_as_cartas3(self, pedir_carta_mock: MagicMock):
        jogador = Player()
        pedir_carta_mock.return_value = {"naipe": "Ouros", "numero": "Valete", "jogador": jogador.name}
        resposta = self.baralho.dar_as_cartas(jogador)
        resposta2 = self.baralho.pedir_carta(jogador)
        resposta3 = self.baralho.pedir_carta(jogador)
        print(resposta, resposta2, resposta3)

    def test_mostrar_cartas(self):
        carta = {"naipe": "Copas", "numero": "Dama", "jogador": None, "id": "0b2a08d4-216a-412b-b02f-284493adf47d"}
        print(self.baralho.cartas)


    def test_pedir_carta(self):
        jogador = Player()
        resposta = self.baralho.pedir_carta(jogador)
        print(resposta)