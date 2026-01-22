saldo = 200
while True:
    valor = float(input('Valor do saque (ou 0 para encerrar): '))
    if valor == 0:
        print('Encerrando...')
        break
    if valor <= 0 or valor % 10 != 0:
        print('Valor inválido, deve ser um múltiplo de 10.')
        continue
    if valor > saldo:
        print('Saldo insuficiente.')
        continue
    saldo = saldo - valor
    print('saque realizado, saldo restante:', saldo)