from baralho import Baralho

def test_somar_pontos_numeros():
    cartas = [
        {"naipe": "Ouros", "numero": 8, "jogador": None},
        {"naipe": "Copas", "numero": 2, "jogador": None},
        {"naipe": "Ouros", "numero": 9, "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 19

def test_somar_pontos_figuras():
    cartas = [
        {"naipe": "Ouros", "numero": "Rei", "jogador": None},
        {"naipe": "Copas", "numero": "Dama", "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 20


def test_soma_pontos_com_as_igual_a_onze():
    cartas = [
        {"naipe": "Ouros", "numero": 1, "jogador": None},
        {"naipe": "Copas", "numero": 9, "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 20

def test_soma_pontos_com_as_igual_a_um():
    cartas = [
        {"naipe": "Ouros", "numero": 9, "jogador": None},
        {"naipe": "Ouros", "numero": 1, "jogador": None},
        {"naipe": "Copas", "numero": 1, "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 21


test_somar_pontos_numeros()

test_somar_pontos_figuras()

test_soma_pontos_com_as_igual_a_onze()

test_soma_pontos_com_as_igual_a_um()


