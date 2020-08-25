from colorama import init


init()
sexo = str(input('Informe o seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dado inválido, por favor, digite novamente.')
    sexo = str(input('Informe o seu sexo[M/F]: ')).strip().upper()[0]
print(f'\033[32mSexo {sexo} registrado com sucesso!\033[m')
