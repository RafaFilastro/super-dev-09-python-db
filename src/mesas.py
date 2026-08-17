from conexao_banco import conectar


def cadastrar():
    print("\n------CADASTRAR MESA------")
    numero = int(input("Número (ex:015): "))
    lugares = int(input("Lugares: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO mesas (numero, lugares) VALUES (%s, %s)",
        (numero, lugares),
    )

    conexao.commit()
    print(f"\n[OK] Mesa cadastrada com id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()

def listar_mesas():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id, numero, lugares
        FROM mesas
        ORDER BY lugares ASC
        """)

    mesa = cursor.fetchall()

    if len(mesa) == 0:
        print("Nenhum mesa cadastrado")
        return

    print("-"*76, end="")
    print(f"\n{'ID':<4} {'NUMERO':<10} {'LUGARES':<10}")
    print("-"*76)
    for mesas in mesa:
        id = mesas[0]
        numero = mesas[1]
        lugares = mesas[2]

        print(
            f"{id:<4} {numero:<10} {lugares:<10}"
        )
    print("-"*76)

def excluir_mesa():
    listar_mesas()

    id_mesa = int(input("Id da mesa que você deseja excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM mesas WHERE id = %s", (id_mesa,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Mesa não encontrada com este id.")
    else:
        print("Registro apagado com sucesso")

def alterar_mesa():
    listar_mesas()

    print("\n------EDITAR MESA------")

    id_mesa = int(input("Id da mesa que você deseja alterar: "))
    numero = int(print("Informe o numero da mesa: "))
    lugares = int(print("Informe a quantidade de lugares: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE mesas SET numero = %s, lugares = %s WHERE id = %s",
        (numero, lugares, id_mesa),
    )
    conexao.commit()
    conexao.close()

    if cursor.rowcount == 0:
        print("Mesa não encontrada com este id")
    else:
        print("Mesa alterado com sucesso")

def menu_mesas():
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
            listar_mesas()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_mesa()
        elif opcao == 4:
            excluir_mesa()
        elif opcao != 5:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))
