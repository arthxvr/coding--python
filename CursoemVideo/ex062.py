print('PROGRESSÃO ARITMÉTICA 2.0')
print('=-' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} - ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos você quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados.')
