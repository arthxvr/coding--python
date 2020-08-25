from random import randint


print('=-' * 25)
print('Pensei em um número entre 0 e 10...Adivinhe qual é...')
print('=-' * 25)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Palpite: '))
    computador = randint(0, 10)
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente.')
        elif jogador > computador:
            print('Menos...Tente novamente.')
print(f'Você acertou com {palpites} palpites. Parabéns!')
