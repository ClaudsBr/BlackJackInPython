import emoji

from baralho import Baralho
from jogador import Jogador
import unittest
from unittest.mock import patch, MagicMock
import random


class TestBaralho(unittest.TestCase):

    def setUp(self):
        random.seed(10)
        self.baralho = Baralho()

    def test_metodo_somar_pontos_usando_apenas_numeros(self):
        cartas = [

            {"naipe": emoji.emojize(":heart_suit:"), "numero": "8", "jogador": None,
             "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "2", "jogador": None,
             "id": "e4d9c608-6019-4ef5-9258-4dc8276f6cc8"},
            {"naipe": emoji.emojize(":spade_suit:"), "numero": "9", "jogador": None,
             "id": "5f036d20-9534-47e1-9d6d-4424cb9298d4"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 19)

    def test_somar_pontos_usando_as_figuras(self):
        cartas = [
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "K", "jogador": None,
             "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "J", "jogador": None,
             "id": "eeb5f5ad-083b-46a0-9b5f-ff63eec12940"}
        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 20)

    def test_somar_pontos_com_as(self):
        cartas = [
            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "8", "jogador": None,
             "id": "a56699ba-bfe7-4346-a830-9998d13a2ad3"},
            {"naipe": emoji.emojize(":spade_suit:"), "numero": "A", "jogador": None,
             "id": "bebb9f09-19ae-46a0-8bab-0bcaa543f4c4"},
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "K", "jogador": None,
             "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},
            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"}
        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 20)

    def test_somar_pontos_21_com_o_valete(self):
        cartas = [

            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "J", "jogador": None,
             "id": "eeb5f5ad-083b-46a0-9b5f-ff63eec12940"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)

    def test_somar_pontos_21_com_o_rei(self):
        cartas = [

            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "K", "jogador": None,
             "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},

        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)

    def test_somar_pontos_22(self):
        cartas = [

            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "K", "jogador": None,
             "id": "3fa5abe8-e948-42ee-a2c8-d72235a5df8f"},
            {"naipe": emoji.emojize(":club_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
        ]
        pontos = self.baralho.somar_pontos(cartas)
        resposta = pontos == 22
        self.assertFalse(resposta)

    def test_somar_pontos_21_dama(self):
        cartas = [

            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "A", "jogador": None,
             "id": "32601ad5-a8c4-462e-811f-eed2914f105f"},
            {"naipe": emoji.emojize(":heart_suit:"), "numero": "Q", "jogador": None,
             "id": "0b2a08d4-216a-412b-b02f-284493adf47d"},
        ]
        pontos = self.baralho.somar_pontos(cartas)
        self.assertEqual(pontos, 21)

    def test_se_o_baralho_tem_o_naipe_de_paus(self):
        achar_paus = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == emoji.emojize(":club_suit:"):
                achar_paus = True

        self.assertTrue(achar_paus)

    def test_se_o_baralho_tem_o_naipe_de_copas(self):
        achar_copas = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == emoji.emojize(":heart_suit:"):
                achar_copas = True

        self.assertTrue(achar_copas)

    def test_se_o_baralho_tem_o_naipe_de_espadas(self):
        achar_espadas = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == emoji.emojize(":spade_suit:"):
                achar_espadas = True

        self.assertTrue(achar_espadas)

    def test_se_o_baralho_tem_o_naipe_de_ouros(self):
        achar_ouros = False
        for carta in self.baralho.cartas:
            if carta['naipe'] == emoji.emojize(":diamond_suit:"):
                achar_ouros = True

        self.assertTrue(achar_ouros)

    def test_quantidade_cartas_do_baralho(self):
        tamanho = len(self.baralho.cartas)
        self.assertEqual(tamanho, 52)

    def test_se_tem_rei_no_baralho(self):
        achar_rei = False
        for carta in self.baralho.cartas:
            if carta["numero"] == "K":
                achar_rei = True

        self.assertTrue(achar_rei)

    def test_se_tem_dama_no_baralho(self):
        achar_dama = False
        for carta in self.baralho.cartas:
            if carta["numero"] == "Q":
                achar_dama = True
        self.assertTrue(achar_dama)

    def test_se_tem_valete_no_baralho(self):
        achar_valete = False
        for carta in self.baralho.cartas:
            if carta['numero'] == "J":
                achar_valete = True
        self.assertTrue(achar_valete)

    def test_se_o_jogador_recebe_carta_do_baralho(self):
        jogador = Jogador()
        cartas = self.baralho.dar_as_cartas(jogador)
        self.assertEqual(jogador.cartas, cartas)

    def test_da_chave_jogador_nas_cartas_do_baralho(self):
        achar_jogador = False
        jogador = Jogador()
        carta = self.baralho.pedir_carta(jogador)
        if carta['jogador'] == jogador.nome:
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
    def test_metodo_dar_as_cartas(self, pedir_carta_mock: MagicMock):
        jogador = Jogador()
        pedir_carta_mock.side_effect = [
            {"naipe": emoji.emojize(":diamond_suit:"), "numero": "J", "jogador": jogador.nome},
            {"naipe": emoji.emojize(":club_suit:"), "numero": "J", "jogador": jogador.nome},
        ]
        resposta = self.baralho.dar_as_cartas(jogador)
        print(resposta)

    @patch("baralho.Baralho.pedir_carta", MagicMock(side_effect=[
        {"naipe": emoji.emojize(":diamond_suit:"), "numero": "J", "jogador": "Claudio"},
        {"naipe": emoji.emojize(":club_suit:"), "numero": "J", "jogador": "Claudio"},
    ]))
    def test_dar_as_cartas(self):
        jogador = Jogador("Claudio")
        resposta = self.baralho.dar_as_cartas(jogador)
        print(resposta)

    @patch("baralho.Baralho.pedir_carta")
    def test_dar_as_cartas3(self, pedir_carta_mock: MagicMock):
        jogador = Jogador()
        pedir_carta_mock.return_value = {"naipe": emoji.emojize(":diamond_suit:"), "numero": "J",
                                         "jogador": jogador.nome}
        resposta = self.baralho.dar_as_cartas(jogador)
        resposta2 = self.baralho.pedir_carta(jogador)
        resposta3 = self.baralho.pedir_carta(jogador)
        print(resposta, resposta2, resposta3)

    def test_metodo_mostrar_cartas(self):
        print(self.baralho.cartas)

    def test_metodo_pedir_carta(self):
        jogador = Jogador()
        resposta = self.baralho.pedir_carta(jogador)
        print(resposta)


