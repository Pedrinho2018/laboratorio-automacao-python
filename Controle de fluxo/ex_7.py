while True:
    print('\n1 - ver status')
    print('2 - reiniciar serviço')
    print('0 - sair')

    opcao = input('Escolha uma opção: ').strip()
    if opcao == '1':
        print('Status: Todos os serviços estão funcionando corretamente.')
    elif opcao == '2':
        print('Reiniciando serviços...')
        print('Serviços reiniciados com sucesso.')
    elif opcao == '0':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')