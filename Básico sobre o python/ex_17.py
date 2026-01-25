SENHA_CORRETA = "123"
TENTATIVAS_MAXIMAS = 3
tentativas = 0
logado = False

while tentativas < TENTATIVAS_MAXIMAS:
    senha = input("Digite a senha: ")

    if senha.strip() == "":
        print("Entrada vazia")
        continue

    if senha == SENHA_CORRETA:
        print("Acesso permitido.")
        logado = True
        break

    tentativas += 1

    if tentativas < TENTATIVAS_MAXIMAS:
        print("Senha incorreta. Tente novamente.")

if not logado:
    print("BLOQUEADO")