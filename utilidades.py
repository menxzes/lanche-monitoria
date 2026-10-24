def normalizar_texto(texto):
    texto = texto.strip()
    texto = texto.casefold()

    palavras = texto.split()
    texto_normalizado = " ".join(palavras)

    return texto_normalizado

def capturar_dados_cliente():
    nome = input("Digite seu nome: ")
    idade = int(input("Insira sua idade: "))

    if idade < 18:
        print("Idade insuficiente.")
        return

    nome_normalizado = normalizar_texto(nome)
    nome = nome_normalizado

    return nome, idade