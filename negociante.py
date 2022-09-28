import random
from config import SALDO_INICIAL_DEALER
from jogador import Jogador

class Negociante(Jogador):

    def __init__(self, bias=0):
        super().__init__("Dealer")
        self.saldo = SALDO_INICIAL_DEALER
        self.bias = bias

    def apostando(self):
        return 0

    def jogando(self):
        if self.valores < 17 + self.bias:
            return 'p'
        else:
            return 'm'



