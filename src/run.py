from bebidas import menu_bebida
from clientes import menu_cliente
from funcionario import menu_funcionario
from mesas import menu_mesas
from pratos_feitos import menu_pratos_feito


def __main():
    mensagem = """----- MENU -----

1 - Funcionario
2 - Pratos feitos
3 - Clientes
4 - Bebidas
5 - Mesas
10 - Sair

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 10:
        if opcao == 1:
            menu_funcionario()
        elif opcao == 2:
            menu_pratos_feito()
        elif opcao == 3:
            menu_cliente()
        elif opcao == 4:
            menu_bebida()
        elif opcao == 5:
            menu_mesas()
        elif opcao != 10:
            print("Opção inválida")
        print("\n")

        opcao = int(input(mensagem))

if __name__ == "__main__":
    __main()
