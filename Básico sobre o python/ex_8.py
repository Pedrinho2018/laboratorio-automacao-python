while True:
 numero = int(input("Digite um número inteiro: "))
 try:
  numero = int(numero)
  break
 except ValueError:
    print("Por favor, digite um número inteiro válido.")
print(f"O dobro de {numero} é {numero * 2}")
print(f"O triplo de {numero} é {numero * 3}")
print(f"O quadrado de {numero} é {numero ** 2}")
print(f"O resto da divisão de {numero} por 5 é {numero % 5}")
