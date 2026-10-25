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

    if nome == "":
        print("Nome vazio.")
        return None

    if idade < 18:
        print("Idade insuficiente.")
        return None

    return nome, idade