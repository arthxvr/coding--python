n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    maior = n1
    print(f'O número {maior} é o maior.')
elif n2 > n1:
    maior = n2
    print(f'O número {maior} é o maior.')
else:
    print('Os números são iguais.')
