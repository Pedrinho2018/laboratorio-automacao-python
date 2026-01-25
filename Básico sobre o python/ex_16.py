SENHA_CORRETA = '123'
tentativas = 0

while True:
    senha = input('Digite a senha: ')
    if senha == SENHA_CORRETA:
        print('Acesso permitido.')
        break

    tentativas  = tentativas + 1

    if tentativas == 3:
        print('Número máximo de tentativas atingido. Acesso bloqueado.')
        break
    print('Senha incorreta. Tente novamente.')