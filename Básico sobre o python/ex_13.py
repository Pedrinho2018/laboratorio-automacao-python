total = float(input('Total da compra: R$ '))
qtd_parcelas = int(input('Número de parcelas (1-12): '))

if qtd_parcelas < 1 or qtd_parcelas > 12:
    print('Número de parcelas inválido.')
else:
    valor = round(total / qtd_parcelas, 2)

    for i in range(1, qtd_parcelas + 1):
        if i == qtd_parcelas:
            parcela = round(total - valor * (qtd_parcelas - 1), 2)
        else:
            parcela = valor

        print(f'Parcela {i}: R$ {parcela:.2f}')
