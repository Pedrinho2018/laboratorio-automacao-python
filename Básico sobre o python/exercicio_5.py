'''Crie um programa que:

Peça ao usuário dois números inteiros
Mostre:

a soma
a multiplicação
o maior dos dois números
o menor dos dois números



Regras:

Use input() → int() para converter
Use as funções max() e min()

Exemplo: max(5, 10) → retorna 10


Use print() para mostrar tudo bonito'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print(f"A soma de {num1} e {num2} é {num1 + num2}")
print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")
print(f"O maior número entre {num1} e {num2} é {max(num1, num2)}")
print(f"O menor número entre {num1} e {num2} é {min(num1, num2)}")
