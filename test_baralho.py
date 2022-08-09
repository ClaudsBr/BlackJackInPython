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


def test_somar_pontos_com_as():
    cartas = [
        {"naipe": "Ouros", "numero": 8, "jogador": None},
        {"naipe": "Ouros", "numero": 1, "jogador": None},
        {"naipe": "Espadas", "numero": "Rei", "jogador": None},
        {"naipe": "Paus", "numero": 1, "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 20



test_somar_pontos_numeros()

test_somar_pontos_figuras()

test_somar_pontos_com_as()




