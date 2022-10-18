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

# FIBONACCI v1
numero_da_sequencia = int(input("Qual termo da sequencia de fibonacci voce quer ?\n"))
sequencia_fibonacci = [0, 1]
for n in range(numero_da_sequencia):
    if n >= 2:
        novo_termo = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
        sequencia_fibonacci.append(novo_termo)

print(sequencia_fibonacci[numero_da_sequencia - 1])
print(sequencia_fibonacci)


# FIBONACCI v2
numero = int(input("Digite o termo da sequancia fibonacci se quer encontrar\n"))
t1 = 0
t2 = 1
t3 = t1 + t2

if numero == 1:
    print(t1)
elif numero == 2:
    print(t2)
else:
    for n in range(numero -2):
        t3 = t1 + t2

        t1 = t2
        t2 = t3
print(t3)

# FATORIAL com FOR
numero = int(input("Digite um numero para saber seu fatorial"))
fatorial = 1
# 5x4x3x2x1
for n in range(1, numero + 1):
    fatorial *= numero
    numero -= 1
print(fatorial)

# FATORIAL com WHILE
numero = int(input('DIgite o numero do fatorial'))
fatorial = 1
while numero >= 1:

    fatorial *= numero
    numero -= 1

print(fatorial)

