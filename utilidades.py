import uuid

def normalizar_texto(texto):
    texto = texto.strip()
    texto = texto.casefold()

    palavras = texto.split()
    texto_normalizado = " ".join(palavras)

    return texto_normalizado

def capturar_dados_cliente():
    nome = normalizar_texto(input("Digite seu nome: "))
    idade = int(input("Insira sua idade: "))
    cpf = input("Informe seu CPF (sem pontos e hífen): ")

    if nome == "":
        print("Nome vazio.")
        return None

    if idade < 18:
        print("Idade insuficiente.")
        return None

    if len(cpf) < 11:
        return None

    return nome, idade, cpf

def capturar_cpf():
    cpf = input("Informe seu CPF (sem pontos e hífen): ")
    
    if len(cpf) < 11:
        return None

    return cpf