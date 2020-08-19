from datetime import date


ano_nasc = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nasc
tempo = ano_nasc + 18
if idade < 18:
    print(f'Você possui {idade} anos de idade e irá se alistar em {tempo}.')
elif idade == 18:
    print(f'Você possui {idade} anos, aliste-se imediatamente.')
elif idade > 18:
    print(f'Você possui {idade} anos e deveria ter se alistado em {tempo}.')
