from random import randint


texto = 'PAR OU ÍMPAR'
print('=-' * 15)
print(f'{texto:^20}')
print('=-' * 15)
vitorias = 0
while True:
    jogador = int(input('Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    print('-' * 50)
    print(f'Você jogou {jogador} e computador {computador}.Total de {total}.', end=' ')
    if total % 2 == 0:
        print('DEU PAR.')
    else:
        print('DEU ÍMPAR.')
    print('-' * 50) 
    if opcao == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Vitórias: {vitorias}.')

