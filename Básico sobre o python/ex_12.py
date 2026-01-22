total = 0.0

while True:
    print('\n1) Adicionar item')
    print('2) ver total')
    print('3) Sair')
    op = input('opção: ')

    if op == '1':
        valor = float(input('valor do item: '))
        total = total + valor
    elif op == '2':
        print('total até agora:', total)
    elif op == '3':
        print('saindo...')
        break
    else:
        print('opção inválida')