from config import SALDO_INICIAL_DEALER
from jogador import Jogador


class Negociante(Jogador):

    def __init__(self, tendencia=0):
        super().__init__("Dealer")
        self.saldo = SALDO_INICIAL_DEALER
        self.tendencia = tendencia

    def apostando(self):
        return 0

    def jogando(self):
        if self.pontuacao < 17 + self.tendencia:
            return 'p'
        else:
            return 'm'

    def negociante_perde(self, jogador: Jogador):
        self.set_saldo(self.get_saldo() - (2* jogador.aposta))

    def continuando(self):
        if self.get_saldo() == 0:
            print(f"Quebrou a banca!!!")
            return 'n'
        else:
            return 's'


