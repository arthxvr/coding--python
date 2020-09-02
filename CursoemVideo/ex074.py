from random import sample


numeros = tuple(sample(range(1, 10), 5))
print(f'Números sorteados: {numeros}')
print(f'Menor número: {min(numeros)}')
print(f'Maior número: {max(numeros)}')

