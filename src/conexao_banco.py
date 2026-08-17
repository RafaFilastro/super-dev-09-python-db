from mysql import connector

# pip install mysql-connector-python
# -----------------------------------------

HOST = "localhost"
PORTA = 3306
USUARIO = "root"
SENHA = "Admin@2026"
BANCO = "restau_calabresa"


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
