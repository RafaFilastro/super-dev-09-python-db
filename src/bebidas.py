from banco_dados import conectar


def cadastrar():
    print("\n------CADASTRAR BEBIDA------")
    nome = input("Digite o nome da bebida: ")
    valor = float(input("Digite o valor da bebida: "))
    tipo = input("Digite o tipo da bebida: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO bebidas (nome, valor, tipo) VALUES (%s, %s, %s)",
        (nome, valor, tipo)
    )

    conexao.commit()
    print(f"\n[OK] Bebida adcionada com sucesso no id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()

def listar_bebidas():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id, nome, valor, tipo
        FROM bebidas
        ORDER BY nome ASC
        """)

    bebidas = cursor.fetchall()

    if len(bebidas) == 0:
        print("Nenhuma bebida cadastrada.")
        return

    print("-"*76, end="")
    print(f"\n{'ID':<4} {'NOME':<30} {'VALOR':>12} {'TIPO':<20}")
    print("-"*76)

    for liquido in bebidas:
        id = liquido[0]
        nome = liquido[1]
        valor = liquido[2]
        tipo = liquido[3]
        print(
            f"{id:<4} {nome:<30} {valor:>12} {tipo:<20}"
        )
    print("-"*76)

def excluir_bebida():
    listar_bebidas()

    id_bebida = int(input("Informe o id da bebida que será excluida: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM bebidas WHERE id = %s", (id_bebida,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Bebida não encontrada com este id.")
    else:
        print("Bebida apagada com sucesso.")


def alterar_bebida():
    listar_bebidas()

    print("\n------ALTERAR BEBIDA------")

    id_bebida = int(input("Digite o id da bebida que deseja alterar: "))

    nome = input("Digite o nome da bebida: ")
    valor = float(input("Digite o valor da bebida: "))
    tipo = input("Digite o tipo da bebida: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE bebidas SET nome = %s, valor = %s, tipo = %s WHERE id = %s",
        (nome, valor, tipo, id_bebida),
    )
    conexao.commit()
    conexao.close()

    if cursor.rowcount == 0:
        print("Bebida não encontrada com este id.")
    else:
        print("Bebida alterada com sucesso.")

def menu_bebida():
    mensagem = """----- MENU -----

1 - Litar
2 - Cadastrar
3 - Editar
4 - Apagar
5 - Voltar

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 5:
        if opcao == 1:
            listar_bebidas()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_bebida()
        elif opcao == 4:
            excluir_bebida()
        elif opcao != 5:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))
