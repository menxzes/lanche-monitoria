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

def cadastrar_cliente(nome, idade, cpf):
    cliente_id = gerar_id_uuid_cliente()

    novo_cliente = {
        "id": cliente_id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf
    }

    clientes.append(novo_cliente)

    return True, "Cliente cadastrado com sucesso!"

def executar_cadastro():
    resultado = capturar_dados_cliente()
    if resultado is None:
        return

    nome, idade, cpf = resultado

    sucesso, mensagem = cadastrar_cliente(nome, idade, cpf)

    print(f"Status: {sucesso}; {mensagem}")

# CRUD: LISTAGEM E BUSCA

def listar_clientes(clientes):
    if not clientes:
        print("Lista vazia. Nenhum cliente cadastrado")
        return
    print(f"{'CPF':<14} | {'NOME':<25} | {'IDADE':<5}")
    print("-" * 50)
    for cliente in clientes:
        print(f"{cliente['cpf']:<14} | {cliente['nome']:<25} | {cliente['idade']:<5}")

def buscar_cliente_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

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
                listar_clientes(clientes)
            elif opcao == "3":
                print("Atualizarção")
            elif opcao == "4":
                print("Deleção")
            elif opcao == "0":
                break
            else:
                print("opção inválida. tente novamente.")