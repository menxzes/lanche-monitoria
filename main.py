from clientes import menu_clientes
from produtos import menu_produtos

def menu_principal():
    while True:
        print("=" * 20)
        print("MENU PRINCIPAL")
        print("1 - Gerenciar clientes")
        print("2 - Gerenciar produtos")
        print("3 - Gerenciar vendas")
        print("4 - Relatórios")
        print("0 - Sair")
        print("=" * 20)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            print("vendas em construção")
        elif opcao == "4":
            print("relatórios em construção")
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("opção inválida. tente novamente.")

# ======================================================

if __name__ == "__main__":
    menu_principal()