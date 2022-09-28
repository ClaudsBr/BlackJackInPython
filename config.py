from os import getenv

NOME_APLICACAO = getenv('NOME_APLICACAO', 'BLACKJACK')
SALDO_INICIAL_JOGADOR = int(getenv(f'{NOME_APLICACAO}_SALDO_INICIAL_JOGADOR', 3000))
SALDO_INICIAL_DEALER = int(getenv(f'{NOME_APLICACAO}_SALDO_INICIAL_DEALER', 100000))