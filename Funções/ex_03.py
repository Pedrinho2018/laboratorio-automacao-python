def montar_msg(nome):
    return f"Olá, {nome}!"
nome = input("Digite seu nome: ")
msg = montar_msg(nome)
print(msg)