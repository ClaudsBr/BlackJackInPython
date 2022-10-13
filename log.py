import logging
from config import NOME_APLICACAO, NIVEL_LOG


FORMAT = '%(asctime)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger(NOME_APLICACAO)
logger.setLevel(NIVEL_LOG)