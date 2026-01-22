prioridade = input('prioridade (P1,P2,P3): ').strip().upper()
if prioridade == 'P1':
    print('incidente critico')
elif prioridade == 'P2':
    print('incidente alto')
elif prioridade == 'P3':
    print('incidente medio')
else:
    print('prioridade invalida')