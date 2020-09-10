lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'Lista de valores na ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
