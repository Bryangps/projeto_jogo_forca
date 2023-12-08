from random import choice
from modulo import *

lista = ['teclado', 'celular', 'avião', 'cachorro', 'carro', 'escola']
sorteio = choice(lista)
minha_lista = []
for v in range(len(sorteio)):
    minha_lista.append('_ ')
print(sorteio)
print(len(sorteio))

#programa principal
cabecalho('JOGO DA FORCA')
objeto(sorteio)
tote = len(sorteio) + 2
contador = 0
while tote > contador:
    letra = verificacao('Digite uma letra para adivinhar:')

    for valores in minha_lista:
        print(valores, end='')
    print()








