total = 0

for n in range(1, 11):
    print('n =', n)

    if n % 2 == 0:
        print('pulando numero par')
        continue
    total += n
print('Total dos numeros impares de 1 a 10 =', total)
print('TOTAL FINAL =', total)