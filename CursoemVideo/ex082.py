pares = []
impares = []
valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = str(input('Quer continuar [S/N] ')).strip().upper()
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if resp in 'Nn':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
