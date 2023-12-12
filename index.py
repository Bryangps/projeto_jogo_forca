from random import choice
from modulo import *

lista = ['teclado', 'celular', 'avião', 'cachorro', 'carro', 'escola']
palavra = choice(lista)
letra_usuario = []


#programa principal
cabecalho('JOGO DA FORCA')
dica(palavra)
chance = 4
ganhou = False
stop = True
while True:
    #try:

    print(f'Você tem {chance} tentativas: ', end='')
    for letra in palavra:
        if letra in letra_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print('')
    tentativas = letra_adivinhar('Digite uma letra para adivinhar:')
    letra_usuario.append(tentativas)

    if tentativas not in palavra:
        chance -= 1
    ganhou = True
    for letra in palavra:
        if letra not in letra_usuario:
            ganhou = False
    if chance == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, você ganhou. A palavra era: \"{palavra}"')
else:
    print(f'Você perdeu. A plavra era \"{palavra}\"')




