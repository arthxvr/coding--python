soma = total = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        total += 1
        print(c, end=' ')
print(f'Soma dos {total} ímpares múltiplos de 3 é {soma}')
