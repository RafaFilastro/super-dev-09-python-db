import os

from dotenv import load_dotenv
from mysql import connector

# pip install mysql-connector-python
# pip install python-dotenv
# --------------------------
# Irá carregar nas variaveis de ambiente as variaveis definada no arquivo .env
load_dotenv()

# Dados da conexão do banco de dados
HOST = os.getenv('BD_HOST')
PORTA = os.getenv('BD_PORTA')
USUARIO = os.getenv('BD_USUARIO')
SENHA = os.getenv('BD_SENHA')
BANCO = os.getenv('BD_BANCO')

def conectar():
    """Abre a conexão com MySQL e retorna ela"""
    conexao = connector.connect(
        host=HOST,
        port=PORTA,
        user=USUARIO,
        password=SENHA,
        database=BANCO,
    )
    return conexao
