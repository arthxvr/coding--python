from random import randint
from time import sleep


print('-=' * 25)
print('ESTOU PENSANDO EM UM NÚMERO...ADIVINHE QUAL É...')
print('-=' * 25)
jogador = int(input('Digite um número entre 0 e 5: '))
computador = randint(0, 5)
print('Analisando jogada...')
sleep(1)
print(f'O computador pensou no número {computador}.')
if jogador == computador:
    print('Parabéns, você venceu!')
else:
    print('O computador venceu.')
