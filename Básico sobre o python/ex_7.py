preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
preco_final = preco * (1 - desconto / 100)
imposto = preco_final * 0.08
preco_com_imposto = preco_final + imposto
print(f"Preço final com desconto: R$ {preco_final:.2f}")
print(f"Preço final com imposto: R$ {preco_com_imposto:.2f}")