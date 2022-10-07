import time
from baralho import Baralho
from jogador import Jogador
import random

import random
import itertools

class ClaudioError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

'''try:
    try:
        test_somar_pontos_21_rei()
    except KeyError as erro:
        print(f'Erro de chave {erro.__class__}')
    except ValueError:
        print("Value Error")
    except Exception:
        print("Exception")
    else:
        print("Else interno")
        raise ClaudioError("Erro123")
except ZeroDivisionError:
    print("Erro")
else:
    print("Else")
finally:
    print("Finalmente")

lista = [1,2,3,4]
buffer = itertools.cycle(lista)
for i in buffer:
    print(i)'''

