maiorpeso = menorpeso = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maiorpeso = menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print(f'Maior peso: {maiorpeso}')
print(f'Menor peso: {menorpeso}')
