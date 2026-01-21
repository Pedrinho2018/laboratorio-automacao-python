'''EXERCÍCIO 3 — input(), int() e operadores (um por vez)
Tarefa:

Peça ao usuário para digitar um número inteiro.
Calcule e imprima (cada um em uma linha):

o dobro desse número
o triplo
o quadrado
o resto da divisão por 5 (use % 5)



Regras:

Use input() para ler.
Converta para int antes de calcular.
Formate a saída bonitinha (pode ser com + ou f-strings, como preferir).'''

numero = int(input("Digite um número inteiro: "))
print(f"O dobro de {numero} é {numero * 2}")
print(f"O triplo de {numero} é {numero * 3}")
print(f"O quadrado de {numero} é {numero ** 2}")
print(f"O resto da divisão de {numero} por 5 é {numero % 5}")