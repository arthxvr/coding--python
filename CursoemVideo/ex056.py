soma = media = maisvelho = mulhermenos20 = 0
nomevelho = ''
for c in range(1, 5):
    nome = str(input(f'Nome da {c}ª pessoa: ')).strip()
    idade = int(input(f'Idade da {c}ª pessoa: '))
    sexo = str(input(f'Sexo da {c}ª pessoa[M/F]: ')).strip().upper()[0]
    soma += idade 
    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
media = soma / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomevelho}')
print(f'Ao todo são {mulhermenos20} mulher(es) com menos de 20 anos.')
