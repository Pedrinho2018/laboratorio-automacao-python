numero = (int(input("Digite um número inteiro: ")))
soma = 0
pares = 0
impares = 0
for i in range(1, numero + 1):
    soma += i
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"A soma dos números de 1 até {numero} é: {soma}")
print(f"A quantidade de números pares entre 1 e {numero} é: {pares}")   
print(f"A quantidade de números ímpares entre 1 e {numero} é: {impares}")
print(f"A média dos números de 1 até {numero} é: {soma / numero:.2f}")
