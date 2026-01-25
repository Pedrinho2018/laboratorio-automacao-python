usuario = "admin"
senha = "123"
MAX = 3
tentativas = 0

while tentativas < MAX:
    user = input("Digite o usuário: ").strip()
    if user == "":
        print("Usuário não pode ser vazio. Tente novamente.")
        continue

    input_senha = input("Digite a senha: ").strip()
    if input_senha == "":
        print("Senha não pode ser vazia. Tente novamente.")
        continue

    if user == usuario and input_senha == senha:
        print("OK")
        break

    tentativas += 1

    if tentativas == MAX:
        print("BLOQUEADO")
        break

    print(f"ERRO. Restam {MAX - tentativas} tentativa(s)")
