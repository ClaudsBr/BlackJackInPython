from baralho import Baralho


def test_somar_pontos_numeros():
    cartas = [
        {"naipe": "Ouros", "numero": "8", "jogador": None},
        {"naipe": "Copas", "numero": "2", "jogador": None},
        {"naipe": "Ouros", "numero": "9", "jogador": None}
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
        {"naipe": "Ouros", "numero": "8", "jogador": None},
        {"naipe": "Ouros", "numero": "1", "jogador": None},
        {"naipe": "Espadas", "numero": "Rei", "jogador": None},
        {"naipe": "Paus", "numero": "1", "jogador": None}
    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 20


def test_somar_pontos_21_valete():
    cartas = [

        {"naipe": "Ouros", "numero": "1", "jogador": None},
        {"naipe": "Espadas", "numero": "Valete", "jogador": None},

    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 21


def test_somar_pontos_21_rei():
    cartas = [

        {"naipe": "Ouros", "numero": "1", "jogador": None},
        {"naipe": "Espadas", "numero": "Rei", "jogador": None},

    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 21


def test_somar_pontos_21_dama():
    cartas = [

        {"naipe": "Ouros", "numero": "1", "jogador": None},
        {"naipe": "Espadas", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    pontos = baralho.somar_pontos(cartas)
    assert pontos == 21

def test_naipe_paus():
    cartas = [

        {"naipe": "Paus", "numero": "1", "jogador": None},
        {"naipe": "Paus", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_naipe_copas():
    cartas = [

        {"naipe": "Copas", "numero": "1", "jogador": None},
        {"naipe": "Copas", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_naipe_espadas():
    cartas = [

        {"naipe": "Espadas", "numero": "1", "jogador": None},
        {"naipe": "Espadas", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_naipe_ouros():
    cartas = [

        {"naipe": "Ouros", "numero": "1", "jogador": None},
        {"naipe": "Ouros", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_valor_maior_que_dez():
    carta = {"naipe": "Paus", "numero": "11", "jogador": None}
    baralho = Baralho()
    achar_cartas = carta in baralho.cartas
    assert achar_cartas == False

def test_valor_rei():
    cartas = [

        {"naipe": "Ouros", "numero": "Rei", "jogador": None},
        {"naipe": "Paus", "numero": "Rei", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_valor_dama():
    cartas = [

        {"naipe": "Ouros", "numero": "Dama", "jogador": None},
        {"naipe": "Paus", "numero": "Dama", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True

def test_valor_valete():
    cartas = [

        {"naipe": "Ouros", "numero": "Valete", "jogador": None},
        {"naipe": "Paus", "numero": "Valete", "jogador": None},

    ]
    baralho = Baralho()
    achar_cartas = (cartas[0] in baralho.cartas) and (cartas[1] in baralho.cartas)
    assert achar_cartas == True