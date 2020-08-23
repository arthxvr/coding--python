from datetime import date


maioridade = menoridade = 0
for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = date.today().year - ano_nasc 
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'{maioridade} pessoas atingiram a maioridade.')
print(f'{menoridade} pessoas atingiram a menoridade.')
