senha_correta = '123'
tentativas = 3

while tentativas > 0:
    senha = input('Digite a senha: ')
    if senha == senha_correta:
        print('Acesso concedido.')
        break
    else:
        tentativas -= 1
        print(f'Senha incorreta. Você tem {tentativas} tentativas restantes.')
if tentativas == 0:
    print('usuario bloqueado.')