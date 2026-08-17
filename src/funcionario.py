from datetime import date

from banco_dados import conectar


def cadastrar():
    print("\n------CADASTRAR FUNCIONARIO------")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: ").replace(",","."))
    data_nascimento = input("Data de nascimento: (ex.:20/12/2000): ")

    data_nascimento_partes = data_nascimento.split("/")
    data_nascimento = f"{data_nascimento_partes[2]}-{data_nascimento_partes[1]}-{data_nascimento_partes[0]}"

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO funcionarios (nome, cargo, salario, data_nascimento) VALUES (%s, %s, %s, %s)",
        (nome, cargo, salario, data_nascimento),
    )

    #Commit é a efetivação do comando no banco de dados
    conexao.commit()
    print(f"\n[OK] Funcionario cadastrado com id: {cursor.lastrowid}")

    # Fechar o curso e a conexão do banco de dados
    cursor.close()
    conexao.close()

def formatar_data(data: date):
    if data is None:
        return"-"
    # Formatar data no padrão pt-br "22/10/2023"
    return data.strftime("%d/%m/%Y")


def listar_funcionarios():
    # Abrir a conexao com o banco de dados
    conexao = conectar()

    # Criar o cursor para poder executar algum comando no banco de dados
    cursor = conexao.cursor()

    # Definir o comando de consulta dos funcionarios
    cursor.execute("""
        SELECT
            id, nome, cargo, salario, data_nascimento
        FROM funcionarios
        ORDER BY nome ASC
        """)

    # fetchall() retorna todas as linhas encontradas naquela consulta
    #cada linha contém uma tupla com onde cada posição é a coluna do select
    funcionarios = cursor.fetchall()

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado")
        return

    print("-"*76, end="")
    print(f"\n{'ID':<4} {'NOME':<22} {'CARGO':<20} {'NASCIMENTO':<15} {'SALARIO':>10}")
    print("-"*76)
    for colaborador in funcionarios:
        id = colaborador[0]
        nome = colaborador[1]
        cargo = colaborador[2] if colaborador[2] else "-"
        salario = colaborador[3] if colaborador[3] else "-"
        data_nascimento = formatar_data(colaborador[4])
        print(
            f"{id:<4} {nome:<22} {cargo:<20} {data_nascimento:<15} {salario:>10}"
        )
    print("-"*76)

def excluir_funcionario():
    listar_funcionarios()

    id_funcionario = int(input("Id do funcionário que você deseja excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id_funcionario,))
    conexao.commit()

    cursor.close()
    conexao.close()

    # rowcount é a quantidade de linhas que foram afetadas
    if cursor.rowcount == 0:
        print("Funcionario não encontrado com este id")
    else:
        print("Registro apagado com sucesso")

def alterar_funcionario():
    listar_funcionarios()

    print("\n------EDITAR FUNCIONARIO------")

    id_funcionario = int(input("Id do funcionário que você deseja alterar: "))
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: ").replace(",","."))
    data_nascimento = input("Data de nascimento: (ex.:20/12/2000): ")

    data_nascimento_partes = data_nascimento.split("/")
    data_nascimento = f"{data_nascimento_partes[2]}-{data_nascimento_partes[1]}-{data_nascimento_partes[0]}"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE funcionarios SET nome = %s, cargo = %s, salario = %s, data_nascimento = %s WHERE id = %s",
        (nome, cargo, salario, data_nascimento, id_funcionario),
    )
    conexao.commit()
    conexao.close()

    if cursor.rowcount == 0:
        print("Funcionário não encontrado com este id")
    else:
        print("Funcionário alterado com sucesso")

def menu_funcionario():
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
            listar_funcionarios()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_funcionario()
        elif opcao == 4:
            excluir_funcionario()
        elif opcao != 5:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))

