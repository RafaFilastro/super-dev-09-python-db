from mysql import connector


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
