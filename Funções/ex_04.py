def validar_nome(nome):
    nome = nome.strip()
    if nome != "" and not nome.isdigit():
        return True
    else:
        return False

nome = input("Digite seu nome: ")

if validar_nome(nome):
    print("Nome válido.")
else:
    print("Nome inválido.")
