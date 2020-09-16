numeros = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite um {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Valores pares digitados: {numeros[0]}')
print(f'Valores ímpares digitados: {numeros[1]}')
