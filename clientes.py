def menu_clientes():
        while True:
            print("=" * 20)
            print("MENU DE CLIENTES")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Atualizar cliente")
            print("4 - Deletar cliente")
            print("0 - Sair")
            print("=" * 20)

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Cadastro")
            elif opcao == "2":
                print("Lista")
            elif opcao == "3":
                print("Atualizarção")
            elif opcao == "4":
                print("Deleção")
            elif opcao == "0":
                break
            else:
                print("opção inválida. tente novamente.")