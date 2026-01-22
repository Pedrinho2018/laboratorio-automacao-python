total = 0
while True:
    n = input('Digite um numero (ou "0" para encerrar): ')
    
    if n == '0':
        break
    total += int(n)
    print('total', total)