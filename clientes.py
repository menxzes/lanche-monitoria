from utilidades import *

clientes = []

# FUNÇÕES AUXILIARES

def gerar_id_uuid_cliente() -> str:
    id_existentes = {c["id"] for c in clientes}

    while True:
        novo_id = uuid.uuid4().hex.upper()
        if novo_id not in id_existentes:
            return novo_id

# CRUD: CADASTRO

def cadastrar_cliente(nome, idade):
    cliente_id = gerar_id_uuid_cliente()

    novo_cliente = {
        "id": cliente_id,
        "nome": nome,
        "idade": idade
    }

    clientes.append(novo_cliente)

    return True, "Cliente cadastrado com sucesso!"

def executar_cadastro():
    resultado = capturar_dados_cliente()
    if resultado is None:
        return

    nome, idade = resultado

    sucesso, mensagem = cadastrar_cliente(nome, idade)

    print(f"Status: {sucesso}; {mensagem}")

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
                executar_cadastro()
            elif opcao == "2":
                print(clientes)
            elif opcao == "3":
                print("Atualizarção")
            elif opcao == "4":
                print("Deleção")
            elif opcao == "0":
                break
            else:
                print("opção inválida. tente novamente.")