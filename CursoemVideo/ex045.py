from random import randint
from time import sleep


print('-=' * 20)
print('{:>20}'.format('JOKENPÔ'))
print('-=' * 20)
print('''Escolha o seu elemento:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
    ''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Opção: '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('*' * 30)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('*' * 30)
if computador == 0: 
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VITÓRIA DO JOGADOR!')
    elif jogador == 2:
        print('VITÓRIA DO COMPUTADOR!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('VITÓRIA DO COMPUTADOR!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VITÓRIA DO JOGADOR')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: 
    if jogador == 0:
        print('VITÓRIA DO JOGADOR!')
    elif jogador == 1:
        print('VITÓRIA DO COMPUTADOR!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
