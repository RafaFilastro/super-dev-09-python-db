from conexao_banco import conectar


def cadastrar():
    print("\n------CADASTRAR CLIENTE-----")

    nome = input("Informe o nome do cliente: ")
    documento = int(input("Informe o numero do seu cpf ou cnpj: "))
    telefone = input("Informe o seu telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO clientes (nome, documento, telefone) VALUES (%s, %s, %s)",
        (nome, documento, telefone),
    )

    conexao.commit()
    print(f"\n[OK] Cliente cadastrado com id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id, nome, documento, telefone
        FROM clientes
        ORDER BY nome ASC
        """)

    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("Nenhum cliente encontrado")
        return

    print("-"*76, end="")
    print(f"\n{'ID':<4} {'NOME':<22} {'DOCUMENTO':<15} {'TELEFONE':<15}")
    print("-"*76)
    for pessoa in clientes:
        id = pessoa[0]
        nome = pessoa[1]
        documento = pessoa[2]
        telefone = pessoa[3]
        print(
            f"{id:<4} {nome:<22} {documento:<15} {telefone:<15}"
        )
    print("-"*76)

def excluir_cliente():
    listar_clientes()

    id_cliente = int(input("Informe o id do cliente que deseja excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Cliente não encontrado com esse id.")
    else:
        print("Cliente apagado com sucesso.")

def alterar_cliente():
    listar_clientes()

    print("\n------EDITAR CLIENTE------")

    id_cliente = int(input("Informe o id do cliente que deseja editar: "))
    nome = input("Digite o nome: ")
    documento = int(input("Informe o número do documento: "))
    telefone = input("Digite o número do telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE clientes SET nome = %s, documento = %s, telefone = %s WHERE id = %s",
        (nome, documento, telefone, id_cliente),
    )
    conexao.commit()
    conexao.close()

    if cursor.rowcount == 0:
        print("Cliente não encontrado com esse id.")
    else:
        print("Cliente alterado com sucesso.")

def menu_cliente():
    mensagem = """------ MENU ------

1 - Listar
2 - Cadastrar
3 - Editar
4 - Apagar
5 - Voltar

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 5:
        if opcao == 1:
            listar_clientes()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_cliente()
        elif opcao == 4:
            excluir_cliente()
        elif opcao != 5:
            print("Opção inválida.")
        print("\n")

        opcao = int(input(mensagem))
