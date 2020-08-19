from datetime import date


ano_nasc = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nasc
print(f'Idade: {idade} anos. Categoria:', end=' ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')  
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
    
