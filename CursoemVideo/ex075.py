num = tuple(int(input(f'Digite o {i}º número: ')) for i in range(1, 5))
print(f'O número 9 foi digitado {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares, end=' ')
