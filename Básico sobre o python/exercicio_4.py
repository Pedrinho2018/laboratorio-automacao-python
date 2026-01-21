'''Peça o primeiro nome do usuário (input()), depois peça a idade.
Imprima exatamente estas três linhas (com os valores corretos):
nome é string (não precisa converter).
idade deve ser convertida para int para somar 1, e depois convertida para str na hora de imprimir (se usar concatenação).
Pode usar f-strings para facilitar'''

print('ola! Qual seu nome?')
nome = input()
idade = int(input("Qual sua idade? "))
print(f"Olá, {nome}!")
print(f"Seu nome tem {len(nome)} letras.")
print(f"Daqui a um ano você terá {idade + 1} anos.")