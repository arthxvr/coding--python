
total18 = homem_total = mulher20_total = idade = 0
while True:
    texto = 'CADASTRO DE PESSOAS'
    print('-=' * 20)
    print(f'{texto:^40}')
    print('-=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    if idade > 18:
        total18 += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if sexo in 'M':
            homem_total += 1
        elif sexo in 'F' and idade < 20:
            mulher20_total += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f"{'FIM DO PROGRAMA':-^30}")
print(f'Pessoas com mais de 18 anos: {total18}')
print(f'Homens cadastrados: {homem_total}')
print(f'Mulheres com menos de 20 anos: {mulher20_total}')

