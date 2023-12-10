from random import choice
from modulo import *

lista = ['teclado', 'celular', 'avião', 'cachorro', 'carro', 'escola']
sorteio = choice(lista)
linha_potilhadas = []
for v in range(len(sorteio)):
    linha_potilhadas.append('_ ')
print(sorteio)
print(len(sorteio))

#programa principal
cabecalho('JOGO DA FORCA')
dica(sorteio)
tentativas = len(sorteio) + 2
cont = 0
while tentativas > 0:
    letra = letra_adivinhar('Digite uma letra para adivinhar:')

    posicao = []
    if letra not in sorteio:
        tentativas -= 1
        print(f'Não tem a letra {letra}')
        if tentativas != 0:
            print(f'Você tem {tentativas} tentativas')
        else:
            print('Você perdeu, suas tentativas acabaram')
    else:
        for indice, valeu in enumerate(sorteio):
            if letra == valeu:
                posicao.append(indice)

        for valor in posicao:
            linha_potilhadas.pop(valor)
            linha_potilhadas.insert(valor, letra)

        for v in linha_potilhadas:
            print(v, end=' ')
        print()







