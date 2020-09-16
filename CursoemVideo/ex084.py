cadastro = list()
dado = list()
maior_peso = menor_peso = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(dado) == 0:
        maior_peso = menor_peso = cadastro[1]
    else:
        if cadastro[1] > maior_peso:
            maior_peso = cadastro[1]
        if cadastro[1] < menor_peso:
            menor_peso = cadastro[1]
    dado.append(cadastro[:])
    cadastro.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break

print(f'Pessoas cadastradas: {len(dado)}')
print(f'O maior peso foi de {maior_peso}Kg. Peso de', end=' ')
for pessoa in dado:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de {menor_peso}Kg. Peso de', end=' ')
for pessoa in dado:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
