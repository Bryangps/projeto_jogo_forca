def cabecalho(msg):
    tote = len(msg) + 4
    print('-' * tote)
    print(f'  {msg}')
    print(f'-' * tote)


def dica(nome):
    if nome == 'teclado':
        print(f'Advinha a palavra! Dica: \"palavra é um objeto que utilizamos para escreve algo.\"')
    elif nome == 'celular':
        print(f'Advinha a palavra! Dica: \"palavra é um objeto que utilizamos todo os dias, não vive sem ele.\"')

    elif nome == 'avião':
        print(f'Advinha a palavra! Dica: \"parece um passaro mais não é, toda hora tem um no ceú.\"')

    elif nome == 'cachorro':
        print(f'Advinha a palavra! Dica: \"melhor amigo do homem.\"')

    elif nome == 'carro':
        print(f'Advinha a palavra! Dica: \"palavra é um objeto que utilizamos sempre, te leva onde você quiser.\"')

    elif nome == 'escola':
        print(f'Advinha a palavra! Dica: \"onde todos nos se dedica para ser alguem no futuro.\"')


def letra_adivinhar(msg):
    while True:
        try:
            letra = str(input(f'{msg} '))[0].lower()
        except (ValueError, TypeError):
            print('\033[31mValor informado invalido\033[m')
        except IndexError:
            print('\033[31mOps campo não pode ficar vazio, digite uma letra do alfabéto\033[m')
        except KeyboardInterrupt:
            print('\nTchau!!! Volte sempre...')
            break
        else:
            if letra.isnumeric():
                print('\033[31mValor informado invalido, digite uma letra do alfabéto\033[m')
            else:
                return letra




