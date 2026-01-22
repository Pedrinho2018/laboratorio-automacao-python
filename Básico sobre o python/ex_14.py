while True:
    nome = input("Digite seu Nome: ").strip()

    if nome == "":
        print("Nome inválido. Tente novamente.")
        continue

    idade_txt = input("Digite sua Idade: ").strip()
    if not idade_txt.isdigit():
        print("Idade inválida. Tente novamente.")
        continue

    idade = int(idade_txt)

    if idade < 1 or idade > 120:
        print("Idade inválida. Tente novamente.")
        continue

    print("CADASTRO REALIZADO COM SUCESSO!")
    print(f"Nome: {nome}, Idade: {idade}")
    break
