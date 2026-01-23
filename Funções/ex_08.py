def confere_senha(senha):
    return senha == 'segredo123'

def tenta_acesso():
    tentativas = 3
    while tentativas > 0:
        senha = input('Digite a senha de acesso: ')
        if confere_senha(senha):
            print('Acesso permitido.')
            return
        tentativas -= 1
        print(f'Senha incorreta. Você tem {tentativas} tentativas restantes.')
    print('Acesso negado.')
tenta_acesso()