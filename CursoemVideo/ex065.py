num = media = cont = soma = 0
resp = '' 
limite = False
while not limite :
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    media = soma / cont
    resp = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        limite = True
print(f'Média: {media:.2f}')
print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')
