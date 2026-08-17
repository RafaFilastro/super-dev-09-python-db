from conexao_banco import conectar


def cadastrar():
    print("\n------CADASTRAR PRATO------")
    nome = input("Nome: ")
    custo = float(input("Valor do prato: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pratos_feitos (nome, custo) VALUES (%s, %s)",
        (nome, custo),
    )

    conexao.commit()
    print(f"\n[OK] Prato feito cadastrado com id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()

def listar_pratos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id, nome, custo
        FROM pratos_feitos
        ORDER BY nome ASC
        """)
    pratos_feitos = cursor.fetchall()

    if len(pratos_feitos) == 0:
        print("Nenhum prato cadastrado")
        return

    print("-"*76, end="")
    print(f"\n{'ID':<5} {'NOME':<40} {'CUSTO':>10}")
    print("-"*76)
    for prato in pratos_feitos:
        id = prato[0]
        nome = prato[1]
        custo = prato[2]
        print(
            f"{id:<5} {nome:<40} {custo:>10}"
        )
    print("-"*76)

def excluir_prato():
    listar_pratos()

    id_prato_feito = int(input("Informe o id do prato que deseja excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM pratos_feitos WHERE id = %s", (id_prato_feito,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Prato não localizado com este ID")
    else:
        print("Prato apagado com sucesso")

def alterar_prato():
    listar_pratos()

    print("\n------EDITAR PRATO------")

    id_prato_feito = int(input("Informe o id do prato que deseja editar: "))
    nome = input("Nome: ")
    custo = float(input("Custo: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE pratos_feitos SET nome = %s, custo = %s WHERE id = %s",
        (nome, custo, id_prato_feito),
    )
    conexao.commit()
    conexao.close()

    if cursor.rowcount == 0:
        print("Prato não localizado com este id.")
    else:
        print("Prato editado com sucesso.")

def menu_pratos_feito():
    mensagem = """----- MENU -----
1 - Listar
2 - Cadastrar
3 - Editar
4 - Apagar
5 - Voltar

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao !=5:
        if opcao == 1:
            listar_pratos()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_prato()
        elif opcao == 4:
            excluir_prato()
        elif opcao != 5:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))

