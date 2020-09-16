from time import sleep


def maior(*num):
    cont = maior = 0
    print('Analisando os valores: ', end='')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else: 
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nO maior valor é {maior}')
    print(f'Foram informados {cont} valores ao todo.') 


maior(7, 5, 3, 2, 1, 4)
maior(4, 7, 0)
