nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print(f'Média = {media:.2f}')
if media < 5:
    print('Reprovado')
elif 5 <= media < 7 :
    print('Recuperação')
else:
    print('Aprovado')
