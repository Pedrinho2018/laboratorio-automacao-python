dia = input('Dia da semana (segunda, terca, quarta, quinta, sexta, sabado, domingo): ').strip().lower()
hora = int(input('Hora (0-23): '))

if (dia == 'sabado' or dia == 'domingo') and hora >= 22:
    print('pode fazer manutenção')
else:
    print('não pode fazer manutenção')