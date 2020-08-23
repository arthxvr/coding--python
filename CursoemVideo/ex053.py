frase = str(input('Frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
