from config import SALDO_INICIAL_JOGADOR
from uuid import uuid4
from faker import Faker
from log import logger


class Jogador:
    def __init__(self, nome=Faker().name()):
        self.nome = nome
        self.__saldo = SALDO_INICIAL_JOGADOR
        self.cartas = []
        self.aposta = 0
        self.pontuacao = 0
        self.id = str(uuid4())
        self.__ativo = True
        logger.debug('Debugando', extra={'user': nome})

    def jogador_ganha(self, aposta):
        self.__saldo += 2 * aposta

    def jogador_empata(self, aposta):
        self.__saldo += aposta

    def __str__(self):
        string_de_retorno = f"Jogador: {self.nome}\n"
        for carta in self.cartas:
            string_de_retorno += f'{carta}\n'
        string_de_retorno += f'Mão: {self.pontuacao}\nSaldo: {self.__saldo}'

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
                if (self.__saldo < aposta) or (aposta < 0):
                    print("Aposta Inválida")
                else:
                    self.__saldo -= aposta
                    self.aposta = aposta
                    return aposta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor

    def continuando(self):
        while True:
            if self.__saldo == 0:
                print(f"Fim de jogo para o jogador {self.nome} que está sem saldo")
                return 'n'

            resposta = input(f"Deseja continuar no jogo {self.nome}? \nS - SIM\nN - NÃO\n")
            if resposta.lower() == 's':
                return 's'
            elif resposta.lower() == 'n':
                return 'n'
            else:
                print("Resposta Inválida")
                continue

    def desativar(self):
        self.__ativo = False

    def status(self):
        return self.__ativo