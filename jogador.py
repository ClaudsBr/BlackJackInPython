from config import SALDO_INICIAL_JOGADOR
from uuid import uuid4
from faker import Faker


class Jogador:
    def __init__(self, nome=Faker().name()):
        self.nome = nome
        self.__saldo__ = SALDO_INICIAL_JOGADOR
        self.cartas = []
        self.aposta = 0
        self.pontuacao = 0
        self.id = str(uuid4())

    def jogador_ganha(self, aposta):
        self.__saldo__ += 2 * aposta

    def jogador_empata(self, aposta):
        self.__saldo__ += aposta

    def __str__(self):
        string_de_retorno = f"Jogador: {self.nome}\n"
        for carta in self.cartas:
            string_de_retorno += f'{carta}\n'
        string_de_retorno += f'Mão: {self.pontuacao}\nSaldo: {self.saldo}'
        return string_de_retorno

    def jogando(self):
        pergunta = input("Digite:\n"
                         "P - PEDIR outra carta\n"
                         "M - MANTER suas cartas\n")
        return pergunta[0].lower()

    def apostando(self):
        while True:
            try:
                aposta = int(input(f"Digite o valor da sua aposta "
                                   f"{self.nome}\n"))
            except ValueError:
                print("Valor não aceito")
            else:
                if (self.__saldo__ < aposta) or (aposta < 0):
                    print("Aposta Inválida")
                else:
                    self.__saldo__ -= aposta
                    self.aposta = aposta
                    return aposta

    def mostrar_saldo(self):
        return self.__saldo__
