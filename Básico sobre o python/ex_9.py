nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
media = (nota_1 + nota_2 + nota_3) / 3
print(f"A média das notas é: {media:.2f}")
if media >= 7.0:
    print("Aprovado")
    if media <= 5.0:
        print("Recuperação")
    else:
        print("Reprovado")