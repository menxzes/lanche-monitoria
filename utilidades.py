import uuid
from clientes import clientes

def normalizar_texto(texto):
    texto = texto.strip()
    texto = texto.casefold()

    palavras = texto.split()
    texto_normalizado = " ".join(palavras)

    return texto_normalizado

def gerar_id_uuid() -> str:
      id_existentes = {c["id"] for c in clientes}

      while True:
          novo_id = uuid.uuid4().hex.upper()
          if novo_id not in id_existentes:
              return novo_id

def capturar_dados_cliente():
    nome = input("Digite seu nome: ")
    idade = int(input("Insira sua idade: "))
    nome_normalizado = normalizar_texto(nome)

    if nome == "":
        print("Nome vazio.")
        return

    if idade < 18:
        print("Idade insuficiente.")
        return

    nome = nome_normalizado

    return nome, idade