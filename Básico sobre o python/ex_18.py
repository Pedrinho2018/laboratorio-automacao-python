SENHA_CORRETA = '123'
MAX = 3
tentativas = 0

while tentativas < MAX:
    senha = input ('Digite a senha: ')

    if senha.strip() == '':
        print('Senha não pode ser vazia. Tente novamente.')
        continue
    if senha == SENHA_CORRETA:
        print('Acesso permitido.')
        break
    tentativas  = tentativas + 1
    if tentativas == MAX:
        print('Número máximo de tentativas atingido. Acesso bloqueado.')
        break
    print(f'Senha incorreta. Você tem {MAX - tentativas} tentativas restantes.')