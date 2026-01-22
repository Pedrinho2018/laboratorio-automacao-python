while True:
    texto = input("Digite algo (ou '0' para encerrar): ")

    if not texto.isdigit():
        print('entrada invalida')
        continue
    numero = int(texto)

    if numero == 0:
        print("Encerrando o programa.")
        break
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")