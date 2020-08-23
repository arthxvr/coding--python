from colorama import init


init()
total = 0
numero = int(input('Número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')        
    print(c, end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
