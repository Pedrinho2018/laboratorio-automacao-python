def tem_acesso(senha):
    senhas_permitidas = ['1234', 'abcd', 'senha123']
    if senha in senhas_permitidas:
        return True
    else:
        return False
senha = input("Digite a senha de acesso: ")
if tem_acesso(senha):
    print("Acesso permitido.")
else:
    print("Acesso negado.")