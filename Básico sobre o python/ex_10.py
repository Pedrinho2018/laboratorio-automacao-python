peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25.0 <= imc < 29.9:
    print("Sobrepeso")
elif 30.0 <= imc < 34.9:
    print("Obesidade grau I")
elif 35.0 <= imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
print(f"Seu IMC é: {imc:.2f}")