from random import randint
from time import sleep


print('-' * 30)
print(f'{"MEGA SENA":^30}')
print('-' * 30)
jogos = []
sorteados = []
total = 1
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while total <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogos:
            jogos.append(numero)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    sorteados.append(jogos[:])
    jogos.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(sorteados):
    print(f'Jogo {i+1}: {l}', end=sleep(1))
print('-=' * 4, ' < BOA SORTE! > ', '-=' * 4)
