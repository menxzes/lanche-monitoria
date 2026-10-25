import uuid
from clientes import clientes

def normalizar_texto(texto):
    texto = texto.strip()
    texto = texto.casefold()

    palavras = texto.split()
    texto_normalizado = " ".join(palavras)

    return texto_normalizado

def gerar_id_uuid_cliente() -> str:
      id_existentes = {c["id"] for c in clientes}

      while True:
          novo_id = uuid.uuid4().hex.upper()
          if novo_id not in id_existentes:
              return novo_id

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