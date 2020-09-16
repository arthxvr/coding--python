from random import randint
from time import sleep


def sortear(lista):
    print('Sorteando 5 valores em uma lista: ', end='')
    for _ in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}')


numeros = []
sortear(numeros)
soma_par(numeros)
