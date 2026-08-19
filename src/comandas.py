# pip install rich
# py -m pip install rich
from rich.console import Console
from rich.table import Table

from banco_dados import conectar
from clientes import listar_clientes
from pratos_feitos import listar_pratos


def cadastrar():
    listar_clientes()

    id_cliente = int(input("Digite o id do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO comandas (id_cliente) VALUES (%s)",
        (id_cliente,),
    )
    conexao.commit()

    comanda_id = cursor.lastrowid
    print(f"Comanda gerada: {comanda_id}")
    cursor.close()
    conexao.close()


def listar_comandas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT
	cod.id,
    cli.nome
FROM comandas AS cod
INNER JOIN clientes AS cli ON (cod.id_cliente = cli.id)""")
    comandas = cursor.fetchall()

    if len(comandas) == 0:
        print("Nenhuma comanda cadastrada")
        return

    tabela = Table("Id", "Cliente", show_header=True)
    tabela.title = "[not italic]:vampire:[/] Comandas [not italic]:vampire:[/]"

    for comanda in comandas:
        # id = comanda[0]
        # nome = comanda[1]
        id, cliente = comanda
        tabela.add_row(str(id), cliente)

    console = Console()
    console.print(tabela)

    cursor.close()
    conexao.close()


def adicionar_prato_feito_comanda():
    listar_pratos()
    id_prato = int(input("Digite o id do prato feito: "))

    listar_comandas()
    id_comanda = int(input("Digite o id da comanda: "))

    quantidade = int(input("Digite a quantidade: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO comandas_pratos_feitos
            (id_prato_feito, id_comanda, quantidade)
        VALUES
            (%s, %s, %s)
        """,
        (id_prato, id_comanda, quantidade),
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Prato adicionado a comanda")


def listar_pratos_das_comandas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT
	cod.id,
    cli.nome,
    pra.nome
FROM comandas AS cod
INNER JOIN clientes AS cli ON (cod.id_cliente = cli.id)
INNER JOIN comandas_pratos_feitos AS codpra ON (codpra.id_comanda = cod.id)
INNER JOIN pratos_feitos AS pra ON (codpra.id_prato_feito = pra.id)
ORDER BY cod.id ASC""")
    comandas_pratos_feitos = cursor.fetchall()

    tabela = Table("Comanda", "Cliente", "Prato")

    for comanda_prato in comandas_pratos_feitos:
        id_comanda, cliente, prato = comanda_prato

        tabela.add_row(str(id_comanda), cliente, prato)

    console = Console()
    console.print(tabela)

    cursor.close()
    conexao.close()


def excluir_comanda():
    pass


def alterar_comanda():
    pass


def menu_comandas():
    mensagem = """----- MENU -----

1 - Litar
2 - Cadastrar
3 - Fazer pedido
4 - Listar pratos dos pedidos
5 - Voltar

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 5:
        if opcao == 1:
            listar_comandas()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            adicionar_prato_feito_comanda()
        elif opcao == 4:
            listar_pratos_das_comandas()
        elif opcao != 5:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))
